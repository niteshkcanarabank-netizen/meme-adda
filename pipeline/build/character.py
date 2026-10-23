"""Owned character for Meme Adda — drawn entirely in code (PIL).

'Bhaiya' — the adda regular. No third-party art, no real-person likeness:
this drawing code IS the asset, and its output carries rights status
cleared_original (see the pilot's clip records in library/clips/).

Expressions: happy | dreamy | shocked | deadpan | sad
Render functions return RGB PIL Images at scene scale.
"""
from PIL import Image, ImageDraw

SKIN = (246, 199, 150)
HAIR = (38, 32, 30)
SHIRT = (38, 110, 180)
PANTS = (52, 56, 66)
WHITE = (255, 255, 255)
DARK = (30, 30, 34)


def draw_bhaiya(size=560, expr="happy"):
    """Draw Bhaiya bust (head + shoulders) centred in a transparent square."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = size // 2
    # shoulders / shirt
    d.rounded_rectangle([cx - size * 0.34, size * 0.72, cx + size * 0.34, size * 1.02],
                        radius=size * 0.16, fill=SHIRT)
    d.rectangle([cx - size * 0.05, size * 0.72, cx + size * 0.05, size * 0.88], fill=WHITE)
    # neck
    d.rectangle([cx - size * 0.085, size * 0.58, cx + size * 0.085, size * 0.74], fill=SKIN)
    # ears
    for sgn in (-1, 1):
        d.ellipse([cx + sgn * size * 0.235 - size * 0.045, size * 0.42,
                   cx + sgn * size * 0.235 + size * 0.045, size * 0.56], fill=SKIN)
    # head
    d.ellipse([cx - size * 0.235, size * 0.10, cx + size * 0.235, size * 0.66], fill=SKIN)
    # hair — flat top sweep
    d.pieslice([cx - size * 0.245, size * 0.06, cx + size * 0.245, size * 0.40],
               start=180, end=360, fill=HAIR)
    d.rectangle([cx - size * 0.245, size * 0.20, cx + size * 0.245, size * 0.235], fill=HAIR)
    # eyes
    ey = size * 0.40
    ex = size * 0.105
    ew = size * 0.052
    if expr == "deadpan":
        for sgn in (-1, 1):
            d.line([cx + sgn * ex - ew, ey, cx + sgn * ex + ew, ey], fill=DARK, width=max(4, size // 90))
    elif expr == "sad":
        for sgn in (-1, 1):
            d.ellipse([cx + sgn * ex - ew * 0.55, ey - ew * 0.4, cx + sgn * ex + ew * 0.55, ey + ew * 0.7], fill=DARK)
    else:
        for sgn in (-1, 1):
            d.ellipse([cx + sgn * ex - ew * 0.62, ey - ew * 0.75, cx + sgn * ex + ew * 0.62, ey + ew * 0.75], fill=DARK)
            d.ellipse([cx + sgn * ex - ew * 0.2, ey - ew * 0.5, cx + sgn * ex + ew * 0.15, ey - ew * 0.15], fill=WHITE)
    # brows
    by = size * 0.315
    if expr == "shocked":
        by = size * 0.285
    if expr == "sad":
        for sgn in (-1, 1):
            d.line([cx + sgn * ex - ew, by + size * 0.02, cx + sgn * ex + ew, by - size * 0.015], fill=DARK, width=max(4, size // 100))
    else:
        for sgn in (-1, 1):
            d.line([cx + sgn * ex - ew, by, cx + sgn * ex + ew, by], fill=DARK, width=max(4, size // 100))
    # nose
    d.line([cx, size * 0.47, cx - size * 0.02, size * 0.52], fill=(214, 160, 110), width=max(3, size // 140))
    # mouth by expression
    my = size * 0.565
    if expr == "happy" or expr == "dreamy":
        d.arc([cx - size * 0.075, my - size * 0.045, cx + size * 0.075, my + size * 0.055], start=15, end=165, fill=DARK, width=max(5, size // 85))
    elif expr == "shocked":
        d.ellipse([cx - size * 0.045, my - size * 0.01, cx + size * 0.045, my + size * 0.075], fill=(120, 40, 40))
    elif expr == "deadpan":
        d.line([cx - size * 0.06, my + size * 0.02, cx + size * 0.06, my + size * 0.02], fill=DARK, width=max(5, size // 90))
    elif expr == "sad":
        d.arc([cx - size * 0.07, my + size * 0.005, cx + size * 0.07, my + size * 0.10], start=195, end=345, fill=DARK, width=max(5, size // 85))
    # rosy cheeks
    for sgn in (-1, 1):
        d.ellipse([cx + sgn * size * 0.155 - size * 0.035, size * 0.50,
                   cx + sgn * size * 0.155 + size * 0.035, size * 0.545], fill=(244, 160, 140))
    return img
