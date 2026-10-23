#!/usr/bin/env python3
"""Intake stage 1 — Google Trends (IN) RSS fetch -> data/trends/<date>/ records.

Manual-run at v1 (config/sources.yaml: watchers are manual). Uses feedparser
from the Gate-3 venv. One JSON record per trending entry, schema-matching the
Gate-2 sample (tr-YYYYMMDD-000). Usage:
    .venv/bin/python pipeline/intake/intake_trends.py [--limit 10]
"""
import argparse, datetime, json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
import feedparser

FEED_URL = "https://trends.google.com/trending/rss?geo=IN"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    date_dir = os.path.join("data", "trends", now.strftime("%Y-%m-%d"))
    os.makedirs(date_dir, exist_ok=True)
    date_tag = now.strftime("%Y%m%d")

    # continue numbering after any records already captured today
    existing = [f for f in os.listdir(date_dir) if f.startswith(f"tr-{date_tag}-")]
    seq = 0
    for f in existing:
        try:
            seq = max(seq, int(f.rsplit("-", 1)[1].split(".")[0]))
        except ValueError:
            pass

    feed = feedparser.parse(FEED_URL)
    written = []
    for entry in feed.entries[: args.limit]:
        seq += 1
        trend_id = f"tr-{date_tag}-{seq:03d}"
        rec = {
            "trend_id": trend_id,
            "captured_at": now.isoformat(),
            "source": {"type": "google_trends_rss", "account": "", "url": FEED_URL},
            "headline": entry.title,
            "language_mix": "unknown",
            "signal": {
                "first_seen_note": "Google Trends 'Trending now' IN feed at capture time",
                "velocity_note": getattr(entry, "ht_approx_traffic", ""),
                "views": 0,
            },
            "format_guess": "",
            "dedupe": {"cluster_id": None, "similar_to": []},
            "status": "captured",
            "notes": "",
        }
        path = os.path.join(date_dir, f"{trend_id}.json")
        with open(path, "w") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=2, sort_keys=True)
        written.append((trend_id, entry.title))
        print(f"{trend_id}  {entry.title}")
    print(f"wrote {len(written)} records to {date_dir}")


if __name__ == "__main__":
    main()
