#!/usr/bin/env python3
"""Bhaiya — Meme Adda's owned character, drawn in code (PIL only).

v2 (23 Oct 2026, founder fix): nitesh — "change the face in starting, it
don't look good." v1 had a bowl-cut hair dome, stick eyebrows, ears stuck
on mid-face and a thin-arc mouth. v2: swept wavy fringe hair, arched
brows, smaller ears at eye level, an open smile with tongue, a proper
nose curve, softer cheeks, a kurta V-collar, and 3x supersampling so the
edges render clean instead of jagged. v1 is kept at character.py.v1.bak.

No third-party art, no real-person likeness: this drawing code IS the
asset, and its output carries rights status cleared_original (see the
clip records in library/clips/). Returns an RGBA image.
Expressions: happy, dreamy, shocked, deadpan, sad.
Face rules: both eyes open and friendly, no winks, no sharp or scary
features, clean geometry.
"""
from PIL import Image, ImageDraw

SS = 3  # supersampling factor for clean edges

SKIN = (243, 196, 146)
SKIN_SHADE = (232, 178, 126)
HAIR = (38, 32, 30)
KURTA = (46, 111, 183)
KURTA_DARK = (36, 90, 152)
COLLAR = (250, 246, 238)
CHEEK = (244, 150, 138, 110)
DARK = (30, 28, 30)
MOUTH_IN = (122, 44, 40)
TONGUE = (232, 120, 118)


_CACHE = {}


def draw_bhaiya(size=620, expr="happy"):
    """Draw Bhaiya at the given width; height = width * 1.28.

    Renders are cached per (size, expr) — scenes paste the same still
    character on every frame, and the 3x supersampled draw is not cheap.
    Callers get a copy, so pasting/mutation never poisons the cache.
    """
    key = (size, expr)
    if key not in _CACHE:
        _CACHE[key] = _draw_bhaiya_uncached(size, expr)
    return _CACHE[key].copy()


def _draw_bhaiya_uncached(size=620, expr="happy"):
    S = SS
    w, h = size * S, int(size * 1.28) * S
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")

    def E(box, **kw):
        d.ellipse([v * S for v in box], **kw)

    def L(pts, **kw):
        d.line([(x * S, y * S) for x, y in zip(pts[::2], pts[1::2])], **kw)

    def A(box, a0, a1, **kw):
        d.arc([v * S for v in box], a0, a1, **kw)

    def P(pts, **kw):
        d.polygon([(x * S, y * S) for x, y in zip(pts[::2], pts[1::2])], **kw)

    def R(box, r, **kw):
        d.rounded_rectangle([v * S for v in box], radius=r * S, **kw)

    # torso — kurta with a V collar
    R((70, 560, 550, 800), 90, fill=KURTA + (255,))
    P((258, 562, 362, 562, 310, 652), fill=COLLAR + (255,))
    L((310, 652, 310, 700), fill=KURTA_DARK + (255,), width=5 * S)
    # neck
    R((262, 452, 358, 585), 18, fill=SKIN_SHADE + (255,))
    # ears — smaller, at eye level
    E((112, 292, 176, 392), fill=SKIN + (255,))
    E((444, 292, 508, 392), fill=SKIN + (255,))
    E((128, 316, 160, 368), fill=SKIN_SHADE + (255,))
    E((460, 316, 492, 368), fill=SKIN_SHADE + (255,))
    # head — a taller, rounder oval
    E((138, 92, 482, 528), fill=SKIN + (255,))
    # hair — swept top with a wavy fringe (scalloped hairline)
    d.pieslice([125 * S, 18 * S, 495 * S, 318 * S], 180, 360, fill=HAIR + (255,))
    for bx, by, br in ((196, 148, 58), (310, 138, 64), (424, 148, 58)):
        E((bx - br, by - br, bx + br, by + br), fill=HAIR + (255,))
    A((150, 60, 470, 300), 190, 320, fill=(20, 17, 16, 255), width=4 * S)

    # cheeks — soft
    E((186, 372, 262, 414), fill=CHEEK)
    E((358, 372, 434, 414), fill=CHEEK)

    # brows — arched, expression-dependent
    bw = 9 * S
    if expr == "shocked":
        A((206, 218, 282, 268), 200, 340, fill=DARK + (255,), width=bw)
        A((338, 218, 414, 268), 200, 340, fill=DARK + (255,), width=bw)
    elif expr == "deadpan":
        L((208, 252, 280, 248), fill=DARK + (255,), width=bw)
        L((340, 248, 412, 252), fill=DARK + (255,), width=bw)
    elif expr == "sad":
        A((206, 232, 282, 282), 220, 330, fill=DARK + (255,), width=bw)
        A((338, 232, 414, 282), 210, 320, fill=DARK + (255,), width=bw)
    else:  # happy / dreamy — raised friendly arcs
        A((206, 226, 282, 276), 200, 340, fill=DARK + (255,), width=bw)
        A((338, 226, 414, 276), 200, 340, fill=DARK + (255,), width=bw)

    # eyes — both open, friendly highlights
    if expr == "dreamy":
        A((212, 296, 276, 348), 10, 170, fill=DARK + (255,), width=9 * S)
        A((344, 296, 408, 348), 10, 170, fill=DARK + (255,), width=9 * S)
    else:
        E((218, 282, 272, 356), fill=DARK + (255,))
        E((348, 282, 402, 356), fill=DARK + (255,))
        E((232, 294, 250, 312), fill=(255, 255, 255, 255))
        E((362, 294, 380, 312), fill=(255, 255, 255, 255))
        if expr == "shocked":
            E((224, 276, 266, 362), outline=DARK + (255,), width=5 * S)
            E((354, 276, 396, 362), outline=DARK + (255,), width=5 * S)
    # nose — a small soft curve
    A((296, 348, 330, 398), 300, 130, fill=(198, 138, 92, 255), width=6 * S)

    # mouth — expression-dependent
    if expr == "happy":
        d.pieslice([248 * S, 388 * S, 372 * S, 486 * S], 0, 180, fill=MOUTH_IN + (255,))
        E((282, 446, 338, 482), fill=TONGUE + (255,))
        A((248, 388, 372, 486), 0, 180, fill=DARK + (255,), width=6 * S)
    elif expr == "dreamy":
        d.pieslice([262 * S, 396 * S, 358 * S, 472 * S], 0, 180, fill=MOUTH_IN + (255,))
        A((262, 396, 358, 472), 0, 180, fill=DARK + (255,), width=6 * S)
    elif expr == "shocked":
        E((282, 402, 338, 470), fill=MOUTH_IN + (255,), outline=DARK + (255,), width=6 * S)
    elif expr == "deadpan":
        L((272, 442, 348, 442), fill=DARK + (255,), width=9 * S)
    elif expr == "sad":
        A((262, 424, 358, 500), 205, 335, fill=DARK + (255,), width=9 * S)

    img = img.resize((size, int(size * 1.28)), Image.LANCZOS)
    return img


if __name__ == "__main__":
    exprs = ["happy", "dreamy", "shocked", "deadpan", "sad"]
    sheet = Image.new("RGB", (620 * 5, int(620 * 1.28)), (250, 248, 242))
    for i, e in enumerate(exprs):
        b = draw_bhaiya(620, e)
        sheet.paste(b, (620 * i, 0), b)
    sheet.save("character-sheet.png")
    print("wrote character-sheet.png")
