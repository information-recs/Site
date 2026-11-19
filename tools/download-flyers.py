#!/usr/bin/env python3
"""Download the event flyers listed in events.json into ../flyers/ and point events.json at the local copies.

Run it from anywhere on your own computer:   python3 tools/download-flyers.py
Optional: `pip install pillow` first and the flyers are resized and saved as small .webp files.
Already-downloaded flyers are skipped, so it is safe to run again after adding new events.
"""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = os.path.join(ROOT, "events.json")
OUT = os.path.join(ROOT, "flyers")
os.makedirs(OUT, exist_ok=True)

try:
    from PIL import Image
except ImportError:
    Image = None
    print("Pillow not installed: flyers will be saved as downloaded (pip install pillow to shrink them).")

events = json.load(open(EVENTS, encoding="utf-8"))
ok = fail = 0
for e in events:
    url = e.get("flyer") or ""
    if not url.startswith("http"):
        continue  # already local, or no flyer
    ext = "webp" if Image else os.path.splitext(url)[1].lstrip(".") or "jpg"
    name = f"{e['id']}.{ext}"
    dest = os.path.join(OUT, name)
    try:
        if not os.path.exists(dest):
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            raw = urllib.request.urlopen(req, timeout=30).read()
            if Image:
                import io
                im = Image.open(io.BytesIO(raw)).convert("RGB")
                im.thumbnail((640, 800))
                im.save(dest, "WEBP", quality=78, method=6)
            else:
                open(dest, "wb").write(raw)
            time.sleep(0.4)
        e["flyer"] = f"flyers/{name}"
        ok += 1
    except Exception as err:
        fail += 1
        print(f"  could not fetch {url}: {err}")

json.dump(events, open(EVENTS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"Done: {ok} flyers local, {fail} failed. events.json updated.")
sys.exit(1 if fail else 0)
