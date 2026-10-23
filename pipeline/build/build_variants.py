#!/usr/bin/env python3
"""Gate-4 pilot VARIANTS — job-20261023-002/003/004.

nitesh's fix instruction on job-20261023-001 (23 Oct 2026, ~21:35 IST):
add a movie/TV reference with credit, try all three, he decides.
Each variant = the pilot's owned setup (clip A) -> a credited reference
still as the reaction beat -> owned deadpan closer -> end card.
Credit placement (founder instruction 23 Oct 2026 ~23:35 IST): NOT inside
the video — the credit goes in the post description (each job's
post_caption carries it as the closing line).
The reference stills are logged as transformative_fair_use_assessed with a
written assessment (library/clips/clip-20261023-004..006) — credited, NOT
licensed; the Content ID claim risk is recorded, not hidden.

Run: .venv/bin/python pipeline/build/build_variants.py
"""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from character import draw_bhaiya

W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def font(sz): return ImageFont.truetype(FONT, sz)
CREAM = (255, 243, 224); COOL = (226, 234, 245); NAVY = (18, 22, 44)
DARK = (32, 30, 34); RED = (198, 44, 44); GREEN = (28, 140, 74); GOLD = (245, 176, 24)

def text_c(d, y, s, sz, fill=DARK, img_w=W):
    f = font(sz)
    box = d.textbbox((0, 0), s, font=f)
    d.text(((img_w - (box[2] - box[0])) / 2 - box[0], y), s, font=f, fill=fill)

def chip(d, x, y, s, fill):
    f = font(54)
    box = d.textbbox((0, 0), s, font=f)
    tw, th = box[2] - box[0], box[3] - box[1]
    d.rounded_rectangle([x, y, x + tw + 56, y + th + 40], radius=26, fill=fill)
    d.text((x + 28 - box[0], y + 18 - box[1]), s, font=f, fill=(255, 255, 255))
    return tw + 56

def phone(d, x, y, w=330, h=560):
    d.rounded_rectangle([x, y, x + w, y + h], radius=36, fill=(24, 24, 28))
    d.rounded_rectangle([x + 14, y + 44, x + w - 14, y + h - 14], radius=24, fill=(245, 248, 252))
    d.text((x + 30, y + 66), "BANK SMS", font=font(30), fill=(120, 128, 140))
    d.text((x + 30, y + 130), "Salary", font=font(46), fill=DARK)
    d.text((x + 30, y + 192), "Credited!", font=font(44), fill=GREEN)
    d.text((x + 30, y + 282), "\u20B9 48,000", font=font(46), fill=DARK)

def coin(d, cx, cy, r=34):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD, outline=(190, 130, 10), width=5)
    d.text((cx - 17, cy - 27), "\u20B9", font=font(48), fill=(140, 95, 5))

def setup_scene(t):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img, "RGBA")
    text_c(d, 120, "Salary aayi\u2026", 96)
    text_c(d, 240, "aur gayab?", 96, fill=RED)
    bh = draw_bhaiya(620, "happy" if t < 4.2 else "shocked")
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
        for (label, at), w_chip in zip(shown, widths):
            chip(d, x, 1450, label, RED)
            x += w_chip + 24
        text_c(d, 1620, "EMI. Bills. Auto-pay.", 62, fill=(90, 90, 100))
    else:
        for i in range(3):
            coin(d, 800 + i * 90, 560 + int(14 * math.sin(t * 5 + i * 1.4)))
    return img

def ref_scene(t, still, credit):
    """Reference still with slow zoom, header line, burned-in credit bar."""
    img = Image.new("RGB", (W, H), (16, 16, 20))
    d = ImageDraw.Draw(img, "RGBA")
    text_c(d, 150, "Balance dekhne ke baad", 70, fill=(240, 240, 240))
    text_c(d, 260, "mera haal:", 78, fill=GOLD)
    # image area 120..1740 vertical centre block
    iw, ih = 1080, int(1080 * still.height / still.width)
    zoom = 1.0 + 0.07 * min(1.0, (t - 5.0) / 5.5)
    sw, sh = int(iw * zoom), int(ih * zoom)
    s = still.resize((sw, sh))
    x0 = (W - iw) // 2
    y0 = 560
    crop = s.crop(((sw - iw) // 2, (sh - ih) // 2, (sw - iw) // 2 + iw, (sh - ih) // 2 + ih))
    img.paste(crop, (x0, y0))
    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle([x0, y0, x0 + iw, y0 + ih], outline=(255, 255, 255), width=6)
    # NO credit inside the video — founder instruction 23 Oct 2026 ~23:35 IST:
    # "Don't give credit in reels or shorts. Instead give the credit in
    # description." The credit lives in each job's post_caption (description).
    if t >= 7.2:
        text_c(d, y0 + ih + 70, "Balance: bas yaadein.", 76, fill=(240, 240, 240))
    return img

def closer_scene(t):
    img = Image.new("RGB", (W, H), COOL)
    d = ImageDraw.Draw(img, "RGBA")
    text_c(d, 150, "Month-end", 92)
    text_c(d, 270, "speedrun complete.", 80, fill=RED)
    bh = draw_bhaiya(620, "deadpan")
    img.paste(bh, (230, 660), bh)
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([340, 1400, 740, 1620], radius=24, fill=(255, 255, 255), outline=DARK, width=5)
    d.rectangle([340, 1400, 740, 1470], fill=RED)
    text_c(d, 1505, "23", 120)
    text_c(d, 1700, "salary gayi. mahina bacha hai.", 50, fill=(90, 90, 100))
    return img

def end_scene(t):
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img, "RGBA")
    text_c(d, 620, "MEME ADDA", 150, fill=GOLD)
    text_c(d, 830, "roz ka adda, roz ka meme.", 58, fill=(235, 238, 245))
    bh = draw_bhaiya(430, "happy")
    img.paste(bh, (325, 1180), bh)
    return img

VARIANTS = [
    ("job-20261023-002", "clip-20261023-004", "Credit: Hera Pheri (2000) \u00A9 Base Industries Group"),
    ("job-20261023-003", "clip-20261023-005", "Credit: Taarak Mehta Ka Ooltah Chashmah \u00A9 Neela Film Productions / Sony SAB"),
    ("job-20261023-004", "clip-20261023-006", "Credit: Panchayat \u00A9 The Viral Fever / Prime Video"),
]
DUR = 17.0

def build(job_id, clip_id, credit):
    still = Image.open(os.path.join("library", "clips", clip_id, "still.jpg")).convert("RGB")
    frames_dir = os.path.join("productions", job_id, "out", "frames")
    os.makedirs(frames_dir, exist_ok=True)
    n = int(DUR * FPS)
    for i in range(n):
        t = i / FPS
        if t < 5.0:
            fr = setup_scene(t)
        elif t < 10.5:
            fr = ref_scene(t, still, credit)
        elif t < 13.5:
            fr = closer_scene(t)
        else:
            fr = end_scene(t)
        fr.save(os.path.join(frames_dir, f"f{i:04d}.jpg"), quality=88)
    # audio — same synth recipe, retimed
    SR = 22050
    audio = np.zeros(int(DUR * SR), dtype=np.float32)
    def tone(f0, f1, start, dur, vol=0.2):
        i0, i1 = int(start * SR), int((start + dur) * SR)
        tt = np.arange(i1 - i0) / SR
        freq = f0 + (f1 - f0) * (tt / dur)
        ph = 2 * np.pi * np.cumsum(freq) / SR
        env = np.minimum(1.0, np.minimum(tt / 0.02, (dur - tt) / 0.05 + 0.2))
        audio[i0:i1] += vol * np.sin(ph) * np.clip(env, 0, 1)
    arp = [523.25, 659.25, 783.99, 659.25]
    for k in range(10):
        tone(arp[k % 4], arp[k % 4], k * 0.5, 0.42, 0.07)
        tone(arp[k % 4] / 2, arp[k % 4] / 2, k * 0.5, 0.42, 0.05)
    for at in (2.2, 3.1, 4.0):
        tone(700, 180, at, 0.14, 0.35)
    tone(620, 140, 5.0, 0.55, 0.22)
    tone(392, 392, 5.3, 0.5, 0.06); tone(311, 311, 6.1, 0.5, 0.06); tone(392, 392, 6.9, 0.5, 0.06)
    for j, f in enumerate([523.25, 659.25, 783.99, 1046.5]):
        tone(f, f, 13.7 + j * 0.13, 0.3, 0.10)
    audio = np.clip(audio, -0.9, 0.9)
    wav_path = os.path.join("productions", job_id, "out", "audio.wav")
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes((audio * 32767).astype(np.int16).tobytes())
    out = os.path.join("productions", job_id, "out", "final.mp4")
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", os.path.join(frames_dir, "f%04d.jpg"),
                    "-i", wav_path, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-c:a", "aac", "-shortest", out], check=True, capture_output=True)
    subprocess.run(["rm", "-rf", frames_dir])
    print("built", out)

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for job_id, clip_id, credit in VARIANTS:
        if only and job_id != only:
            continue
        build(job_id, clip_id, credit)
