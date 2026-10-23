#!/usr/bin/env python3
"""Gate 3 smoke tests for meme-adda.

Run with the repo venv:  .venv/bin/python pipeline/smoke_tests.py
Each stage prints PASS/FAIL with a reason. A failure is reported, never hidden.
No production assets are used; all fixtures are generated locally.
"""
import sys, os, json, traceback
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
RESULTS = {}

def record(stage, ok, detail):
    RESULTS[stage] = {"pass": bool(ok), "detail": str(detail)[:500]}
    print(f"[{'PASS' if ok else 'FAIL'}] {stage}: {detail}")

# ---------- 1. intake ----------
try:
    import feedparser
    feed = feedparser.parse("https://trends.google.com/trending/rss?geo=IN")
    n = len(feed.entries)
    if n > 0:
        record("intake_trends_rss", True, f"{n} trending entries, first: {feed.entries[0].title!r}")
    else:
        record("intake_trends_rss", False, "feed parsed but 0 entries")
except Exception as e:
    record("intake_trends_rss", False, repr(e))

try:
    import praw
    record("intake_praw_import", True, f"praw {praw.__version__} imports; live subreddit fetch needs Reddit app credentials (owner step)")
except Exception as e:
    record("intake_praw_import", False, repr(e))

try:
    import yt_dlp
    record("intake_ytdlp_import", True, f"yt-dlp {yt_dlp.version.__version__} imports")
except Exception as e:
    record("intake_ytdlp_import", False, repr(e))

# ---------- 2. dedupe ----------
TMP = "/tmp/meme_adda_smoke"
os.makedirs(TMP, exist_ok=True)
try:
    from PIL import Image, ImageDraw
    p = os.path.join(TMP, "fixture.png")
    img = Image.new("RGB", (320, 320), (240, 240, 240))
    d = ImageDraw.Draw(img); d.ellipse([80, 80, 240, 240], fill=(200, 40, 40))
    img.save(p)
    import imagehash
    h1 = str(imagehash.phash(Image.open(p)))
    h2 = str(imagehash.phash(Image.open(p)))
    record("dedupe_imagehash", h1 == h2, f"phash stable: {h1}")
except Exception as e:
    record("dedupe_imagehash", False, repr(e))

try:
    # make a tiny video fixture with ffmpeg (present on the box)
    import subprocess
    vp = os.path.join(TMP, "fixture.mp4")
    if not os.path.exists(vp):
        subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=blue:s=320x320:d=2",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
                        "-shortest", "-pix_fmt", "yuv420p", vp],
                       check=True, capture_output=True)
    import compat  # noqa: F401  (Pillow ANTIALIAS shim for videohash, see pipeline/compat.py)
    from videohash import VideoHash
    v1 = VideoHash(path=vp).hash
    v2 = VideoHash(path=vp).hash
    record("dedupe_videohash", v1 == v2, f"videohash stable: {v1}")
except Exception as e:
    record("dedupe_videohash", False, repr(e))

# ---------- 3. captions ----------
try:
    import subprocess
    ap = os.path.join(TMP, "speech.wav")
    # use ffmpeg's built-in flite TTS if available, else a tone (transcription will be empty but pipeline runs)
    r = subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=220:duration=5",
                        "-ar", "16000", ap], capture_output=True)
    from faster_whisper import WhisperModel
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, info = model.transcribe(ap)
    segs = list(segments)
    record("caption_faster_whisper", True, f"tiny model ran, lang={info.language}, {len(segs)} segments on synthetic audio")
except Exception as e:
    record("caption_faster_whisper", False, repr(e))

try:
    import whisperx
    record("caption_whisperx_import", True, f"whisperx {getattr(whisperx, '__version__', 'unknown')} imports")
except Exception as e:
    record("caption_whisperx_import", False, repr(e))

# ---------- 4. build (9:16 render from an owned, generated asset) ----------
try:
    from moviepy import ColorClip, TextClip, CompositeVideoClip
    out = os.path.join(TMP, "build_test_916.mp4")
    clip = ColorClip(size=(1080, 1920), color=(24, 24, 32), duration=2)
    clip.write_videofile(out, fps=24, codec="libx264", audio=False, logger=None)
    import subprocess
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                            "-show_entries", "stream=width,height", "-of", "csv=p=0", out],
                           capture_output=True, text=True)
    dims = probe.stdout.strip()
    record("build_moviepy_916", dims == "1080,1920", f"rendered {out}, ffprobe={dims}")
except Exception as e:
    record("build_moviepy_916", False, repr(e) + traceback.format_exc()[-200:])

print("\n=== SUMMARY ===")
print(json.dumps(RESULTS, indent=2))
failed = [k for k, v in RESULTS.items() if not v["pass"]]
print("FAILED:", failed if failed else "none")
sys.exit(1 if failed else 0)
