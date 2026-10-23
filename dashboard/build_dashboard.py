#!/usr/bin/env python3
"""Build the static trend dashboard (v1, low-tech).

Reads JSON under data/, library/, productions/ and emits one static
dashboard/site/index.html. No dependencies beyond the stdlib.
Re-run after each posting session:  python3 dashboard/build_dashboard.py
"""
import json
import html
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "dashboard" / "site"
IST = timezone(timedelta(hours=5, minutes=30))


def load_json_dir(path, pattern="*.json"):
    records = []
    if path.exists():
        for f in sorted(path.rglob(pattern)):
            try:
                records.append(json.loads(f.read_text()))
            except Exception:
                pass
    return records


def esc(s):
    return html.escape(str(s or ""))


def panel(title, body):
    return f"<section><h2>{esc(title)}</h2>{body}</section>"


def main():
    trends = load_json_dir(ROOT / "data" / "trends")
    posts = load_json_dir(ROOT / "data" / "posts")
    templates = [json.loads((ROOT / "library" / "templates" / d / "template.json").read_text())
                 for d in (ROOT / "library" / "templates").iterdir()
                 if (d / "template.json").exists()]
    jobs = [json.loads((ROOT / "productions" / d / "job.json").read_text())
            for d in (ROOT / "productions").iterdir() if (d / "job.json").exists()]

    now = datetime.now(IST)

    # Panel 1: trending now
    active = [t for t in trends if t.get("status") in ("new", "shortlisted")]
    rows = "".join(
        f"<li><b>{esc(t.get('trend_id'))}</b> [{esc(t.get('status'))}] "
        f"{esc(t.get('headline'))} <i>first seen: {esc(t.get('signal', {}).get('first_seen_note'))}</i></li>"
        for t in sorted(active, key=lambda x: x.get("trend_id", ""), reverse=True))
    bodies = [panel("Trending now", f"<ul>{rows or '<li>none</li>'}</ul>")]

    # Panel 2: pipeline status
    by_status = {}
    for j in jobs:
        by_status.setdefault(j.get("status", "?"), []).append(j.get("job_id"))
    stage_rows = "".join(
        f"<li><b>{esc(s)}</b>: {', '.join(esc(i) for i in ids)}</li>"
        for s, ids in sorted(by_status.items()))
    bodies.append(panel("Pipeline status", f"<ul>{stage_rows or '<li>no jobs yet</li>'}</ul>"))

    # Panel 3: posted & verified
    post_rows = ""
    for p in sorted(posts, key=lambda x: x.get("post_id", ""), reverse=True):
        v = p.get("verification", {})
        flag = ""
        if v.get("status") == "pending":
            flag = " <b style='color:red'>PENDING — chase if &gt;2h</b>"
        claim = " [CLAIM]" if p.get("claims", {}).get("content_id_claim") else ""
        post_rows += (f"<li><b>{esc(p.get('post_id'))}</b> {esc(p.get('platform'))} "
                      f"<a href='{esc(p.get('live_url'))}'>live</a> — {esc(v.get('status'))}"
                      f"{flag}{claim}</li>")
    bodies.append(panel("Posted & verified", f"<ul>{post_rows or '<li>none</li>'}</ul>"))

    # Panel 4: metrics/templates
    tpl_rows = "".join(
        f"<li><b>{esc(t.get('template_id'))}</b> — used {t.get('usage_count', 0)}x. "
        f"{esc(t.get('performance_note') or 'no data yet')}</li>" for t in templates)
    bodies.append(panel("Templates", f"<ul>{tpl_rows or '<li>none</li>'}</ul>"))

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Meme Adda — dashboard</title>
<style>body{{font-family:system-ui,sans-serif;max-width:900px;margin:2em auto;padding:0 1em}}
section{{border:1px solid #ccc;border-radius:8px;padding:1em;margin-bottom:1em}}</style></head>
<body><h1>Meme Adda — trend dashboard</h1>
<p>Generated {now.strftime('%Y-%m-%d %H:%M %Z')} from <code>data/</code>. Static v1.</p>
{''.join(bodies)}</body></html>"""
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(page)
    print(f"wrote {SITE / 'index.html'} ({len(trends)} trends, {len(posts)} posts)")


if __name__ == "__main__":
    main()
