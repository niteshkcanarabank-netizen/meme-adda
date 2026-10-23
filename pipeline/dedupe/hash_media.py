#!/usr/bin/env python3
"""Dedupe stage — perceptual hashes into data/hashes/<date>.json.

Runs at intake and again pre-posting (config/thresholds.yaml). For a built
job it records the final video's videohash + the first frame's pHash, which
is the second dedupe pass docs/WORKFLOW.md requires after build.

Usage: .venv/bin/python pipeline/dedupe/hash_media.py productions/job-20261023-001/out/final.mp4
"""
import datetime, json, os, subprocess, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import compat  # noqa: F401  Pillow ANTIALIAS shim for videohash


def main(path):
    from PIL import Image
    import imagehash
    from videohash import VideoHash

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    tmp_frame = "/tmp/dedupe_first_frame.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path, "-frames:v", "1", tmp_frame], check=True)
    phash = str(imagehash.phash(Image.open(tmp_frame)))
    vhash = VideoHash(path=path).hash

    entry = {
        "file": path,
        "hashed_at": now.isoformat(),
        "phash_frame1": phash,
        "videohash": vhash,
        "near_duplicates_in_index": [],
    }
    os.makedirs(os.path.join("data", "hashes"), exist_ok=True)
    idx_path = os.path.join("data", "hashes", f"{now.strftime('%Y-%m-%d')}.json")
    index = []
    if os.path.exists(idx_path):
        with open(idx_path) as fh:
            index = json.load(fh)
    # near-duplicate check against everything already in today's index
    def hamming(a, b):
        return bin(int(a, 16) ^ int(b, 16)).count("1") if a and b else 999

    for other in index:
        if other["file"] != path and hamming(phash, other.get("phash_frame1", "")) <= 8:
            entry["near_duplicates_in_index"].append(other["file"])
    index = [e for e in index if e["file"] != path] + [entry]
    with open(idx_path, "w") as fh:
        json.dump(index, fh, indent=2, sort_keys=True)
    print(json.dumps(entry, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
