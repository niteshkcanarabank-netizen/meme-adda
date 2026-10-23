#!/usr/bin/env python3
"""Gate-4 pilot builder — job-20261023-001 'Salary aayi... aur gayab?'

Template: tpl-two-clip-connect (setup -> OWNED payoff). Every visual is drawn
in code (pipeline/build/character.py + this file); every sound is synthesised
in numpy. No third-party asset enters this build — see the job's clip records
(library/clips/clip-20261023-001..003, all cleared_original).

Copy: ChatGPT (incharge) ruling, research/gate4-pilot-consult-ruling.txt.
Run: .venv/bin/python pipeline/build/build_pilot.py
Out: productions/job-20261023-001/out/final.mp4 (1080x1920, ~14.5s)
"""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from character import draw_bhaiya

W, H, FPS = 1080, 1920, 24
JOB = os.path.join("productions", "job-20261023-001")
FRAMES = os.path.join(JOB, "out", "frames")
os.makedirs(FRAMES, exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def font(sz): return ImageFont.truetype(FONT, sz)

CREAM = (255, 243, 224); COOL = (226, 234, 245); NAVY = (18, 22, 44)
DARK = (32, 30, 34); RED = (198, 44, 44); GREEN = (28, 140, 74); GOLD = (245, 176, 24)

def text_c(d, y, s, sz, fill=DARK, stroke=0, stroke_fill=(255, 255, 255)):
    f = font(sz)
    box = d.textbbox((0, 0), s, font=f, stroke_width=stroke)
    tw = box[2] - box[0]
    d.text(((W - tw) / 2 - box[0], y), s, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return box[3] - box[1]

def chip(d, x, y, s, fill):
    f = font(54)
    box = d.textbbox((0, 0), s, font=f)
    tw, th = box[2] - box[0], box[3] - box[1]
    d.rounded_rectangle([x, y, x + tw + 56, y + th + 40], radius=26, fill=fill)
    d.text((x + 28 - box[0], y + 18 - box[1]), s, font=f, fill=(255, 255, 255))
    return tw + 56, th + 40

def phone(d, x, y, w=330, h=560, credited=True):
    d.rounded_rectangle([x, y, x + w, y + h], radius=36, fill=(24, 24, 28))
    d.rounded_rectangle([x + 14, y + 44, x + w - 14, y + h - 14], radius=24, fill=(245, 248, 252))
    d.text((x + 30, y + 66), "BANK SMS", font=font(30), fill=(120, 128, 140))
    if credited:
        d.text((x + 30, y + 130), "Salary", font=font(46), fill=DARK)
        d.text((x + 30, y + 192), "Credited!", font=font(44), fill=GREEN)
        d.text((x + 30, y + 282), "\u20B9 48,000", font=font(46), fill=DARK)
    else:
        d.text((x + 30, y + 130), "Balance:", font=font(44), fill=DARK)
        d.text((x + 30, y + 206), "\u20B9 212", font=font(54), fill=RED)
        d.text((x + 30, y + 306), "bas yaadein", font=font(36), fill=(120, 128, 140))

def coin(d, cx, cy, r=34):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD, outline=(190, 130, 10), width=5)
    d.text((cx - 17, cy - 27), "\u20B9", font=font(48), fill=(140, 95, 5))

def scene(t):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img, "RGBA")
    if t < 5.0:  # ---- Clip A: setup
        text_c(d, 120, "Salary aayi\u2026", 96)
        text_c(d, 240, "aur gayab?", 96, fill=RED)
        expr = "happy" if t < 4.2 else "shocked"
        bh = draw_bhaiya(620, expr)
        img.paste(bh, (70, 700), bh)
        d = ImageDraw.Draw(img, "RGBA")
        phone(d, 645, 760)
        if t >= 2.0:
            stamps = [("EMI \u2713", 2.2), ("BILLS \u2713", 3.1), ("AUTO-PAY \u2713", 4.0)]
            shown = [s for s in stamps if t >= s[1]]
            f54 = font(54)
            widths = [d.textbbox((0, 0), s, font=f54)[2] + 56 for s, _ in shown]
            total = sum(widths) + 24 * (len(shown) - 1)
            x = max(30, (W - total) // 2)
            y = 1450
            for (label, at), w_chip in zip(shown, widths):
                chip(d, x, y, label, RED)
                x += w_chip + 24
            text_c(d, 1620, "EMI. Bills. Auto-pay.", 62, fill=(90, 90, 100))
        else:
            for i in range(3):
                bob = int(14 * math.sin(t * 5 + i * 1.4))
                coin(d, 800 + i * 90, 560 + bob)
    elif t < 11.0:  # ---- Clip B: payoff (owned)
        img = Image.new("RGB", (W, H), COOL)
        d = ImageDraw.Draw(img, "RGBA")
        if t < 8.0:
            text_c(d, 130, "Balance:", 92)
            text_c(d, 250, "bas yaadein.", 92, fill=RED)
            bh = draw_bhaiya(640, "shocked")
            img.paste(bh, (220, 640), bh)
            d = ImageDraw.Draw(img, "RGBA")
            # empty wallet
            d.rounded_rectangle([330, 1400, 750, 1560], radius=28, fill=(122, 78, 44))
            d.rounded_rectangle([360, 1424, 720, 1500], radius=18, fill=(226, 205, 175))
            roll = int((t - 5.0) * 130) % 700
            coin(d, 140 + roll, 1660)
            text_c(d, 1720, "ek sikka bhaag gaya\u2026", 50, fill=(90, 90, 100))
        else:
            text_c(d, 150, "Month-end", 92)
            text_c(d, 270, "speedrun complete.", 80, fill=RED)
            bh = draw_bhaiya(620, "deadpan")
            img.paste(bh, (230, 660), bh)
            d = ImageDraw.Draw(img, "RGBA")
            # calendar card
            d.rounded_rectangle([340, 1400, 740, 1620], radius=24, fill=(255, 255, 255), outline=DARK, width=5)
            d.rectangle([340, 1400, 740, 1470], fill=RED)
            text_c(d, 1505, "23", 120)
            text_c(d, 1700, "salary gayi. mahina bacha hai.", 50, fill=(90, 90, 100))
    else:  # ---- end card
        img = Image.new("RGB", (W, H), NAVY)
        d = ImageDraw.Draw(img, "RGBA")
        text_c(d, 620, "MEME ADDA", 150, fill=GOLD)
        text_c(d, 830, "roz ka adda, roz ka meme.", 58, fill=(235, 238, 245))
        bh = draw_bhaiya(430, "happy")
        img.paste(bh, (325, 1180), bh)
    return img

DUR = 14.5
n = int(DUR * FPS)
for i in range(n):
    scene(i / FPS).save(os.path.join(FRAMES, f"f{i:04d}.jpg"), quality=88)
print(f"frames: {n}")

# ---------------- audio: all synthesised ----------------
SR = 22050
audio = np.zeros(int(DUR * SR), dtype=np.float32)

def tone(f0, f1, start, dur, vol=0.20, wave_type="sine"):
    i0, i1 = int(start * SR), int((start + dur) * SR)
    tt = np.arange(i1 - i0) / SR
    freq = f0 + (f1 - f0) * (tt / dur)
    ph = 2 * np.pi * np.cumsum(freq) / SR
    env = np.minimum(1.0, np.minimum(tt / 0.02, (dur - tt) / 0.05 + 0.2))
    audio[i0:i1] += vol * np.sin(ph) * np.clip(env, 0, 1)

def pop(at):
    tone(700, 180, at, 0.14, vol=0.35)

# cheerful arp bed, scene A (C major) then sparse B, end sting
arp = [523.25, 659.25, 783.99, 659.25]
for k in range(10):
    f = arp[k % 4]
    tone(f, f, k * 0.5, 0.42, vol=0.07)
    tone(f / 2, f / 2, k * 0.5, 0.42, vol=0.05)
for k in range(6):  # scene B, slower minor
    f = [440.0, 349.23, 440.0, 329.63][k % 4]
    tone(f, f, 5.0 + k * 0.95, 0.7, vol=0.05)
for at in (2.2, 3.1, 4.0):
    pop(at)
tone(620, 140, 5.0, 0.55, vol=0.22)        # wah descend at payoff cut
for j, f in enumerate([523.25, 659.25, 783.99, 1046.5]):
    tone(f, f, 11.1 + j * 0.13, 0.3, vol=0.10)  # end-card sting

audio = np.clip(audio, -0.9, 0.9)
wav_path = os.path.join(JOB, "out", "audio.wav")
with wave.open(wav_path, "wb") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
    wf.writeframes((audio * 32767).astype(np.int16).tobytes())

out = os.path.join(JOB, "out", "final.mp4")
subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", os.path.join(FRAMES, "f%04d.jpg"),
                "-i", wav_path, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
                "-c:a", "aac", "-shortest", out], check=True, capture_output=True)
print("built", out)
