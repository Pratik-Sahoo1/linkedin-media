#!/usr/bin/env python3
"""Render a 1200x1200 LinkedIn market card PNG from a card.json file.

Usage: python tools/render_card.py posts/<date>/card.json
Writes posts/<date>/card.png next to the JSON.
JSON fields: kicker, headline, indices[{name,value,change}], section_title, bullets[], footer
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont

FONT_DIRS = ["/usr/share/fonts/truetype/dejavu/"]
def font(bold, size):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def fit(draw, text, bold, size, max_w):
    while size > 14 and draw.textlength(text, font=font(bold, size)) > max_w:
        size -= 1
    return font(bold, size)

def render(path):
    c = json.load(open(path, encoding="utf-8"))
    W, H = 1200, 1200
    bg, card, white, grey = (15, 23, 42), (30, 41, 59), (241, 245, 249), (148, 163, 184)
    red, green = (248, 113, 113), (74, 222, 128)
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    d.text((70, 70), c.get("kicker", ""), font=fit(d, c.get("kicker", ""), True, 34, 1060), fill=grey)
    d.text((70, 130), c.get("headline", ""), font=fit(d, c.get("headline", ""), True, 62, 1060), fill=white)
    y = 260
    for idx in c.get("indices", [])[:2]:
        d.rounded_rectangle((70, y, 1130, y + 210), radius=24, fill=card)
        d.text((110, y + 25), idx["name"], font=font(True, 38), fill=grey)
        d.text((110, y + 85), idx["value"], font=font(True, 90), fill=white)
        col = red if idx["change"].strip().startswith("-") else green
        d.text((700, y + 110), idx["change"], font=font(True, 56), fill=col)
        y += 240
    d.text((70, 770), c.get("section_title", "What moved the market"), font=font(True, 40), fill=white)
    y = 840
    for t in c.get("bullets", [])[:4]:
        d.ellipse((74, y + 14, 92, y + 32), fill=red)
        d.text((110, y), t, font=fit(d, t, False, 31, 1000), fill=white)
        y += 68
    foot = c.get("footer", "For information only, not investment advice.")
    d.text((70, 1130), foot, font=fit(d, foot, False, 22, 1060), fill=grey)
    out = os.path.join(os.path.dirname(path), "card.png")
    im.save(out, optimize=True)
    print("wrote", out)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        render(p)
