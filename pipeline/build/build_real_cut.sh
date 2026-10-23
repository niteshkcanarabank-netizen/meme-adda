#!/usr/bin/env bash
# Gate-4 pilot — REAL-FOOTAGE cut (job-20261023-005).
# Founder direction 23 Oct 2026 ~23:44 IST: "Do we really need this pic —
# change this to real videos or images." The drawn Bhaiya scenes are
# replaced with licensed stock video (Pexels, clips 007/008); the
# Panchayat reference beat is reused from job-20261023-004; the end card
# is plain text (no character). No credit inside the video — the credit
# lives in the post description (job.json post_caption).
set -euo pipefail
cd "$(dirname "$0")/../.."
JOB=productions/job-20261023-005
TMP=$JOB/out/tmp
mkdir -p "$TMP"
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
W=1080; H=1920; FPS=24

# Text files written via python3 (UTF-8) — bash printf mangled \u escapes
# into literal "u2026"/"u2713" text in the first build (caught on frame review).
python3 - "$TMP" <<'PYEOF'
import sys, os
tmp = sys.argv[1]
texts = {
    "t1": "Salary aayi\u2026", "t2": "aur gayab?",
    "s1": "EMI \u2713", "s2": "BILLS \u2713", "s3": "AUTO-PAY \u2713",
    "t3": "EMI. Bills. Auto-pay.", "t4": "Month-end",
    "t5": "speedrun complete.", "t6": "salary gayi. mahina bacha hai.",
    "t7": "MEME ADDA", "t8": "roz ka adda, roz ka meme.",
}
for k, v in texts.items():
    open(os.path.join(tmp, k + ".txt"), "w", encoding="utf-8").write(v)
PYEOF

DT="fontfile=$FONT:fontcolor=white:borderw=6:bordercolor=black:x=(w-text_w)/2"

# 1) setup 0-5s — smiling man + phone (stock, looped), stamps land 2.0/3.1/4.0
ffmpeg -y -v error -stream_loop 2 -i library/clips/clip-20261023-007/clip.mp4 -t 5 \
  -vf "scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,fps=$FPS,\
drawtext=$DT:textfile=$TMP/t1.txt:fontsize=98:y=110,\
drawtext=$DT:textfile=$TMP/t2.txt:fontsize=98:fontcolor=0xE33E3E:y=235,\
drawtext=fontfile=$FONT:textfile=$TMP/s1.txt:fontsize=52:fontcolor=white:box=1:boxcolor=0xC62C2C:boxborderw=14:x=40:y=1540:enable='gte(t,2.0)',\
drawtext=fontfile=$FONT:textfile=$TMP/s2.txt:fontsize=52:fontcolor=white:box=1:boxcolor=0xC62C2C:boxborderw=14:x=310:y=1540:enable='gte(t,3.1)',\
drawtext=fontfile=$FONT:textfile=$TMP/s3.txt:fontsize=52:fontcolor=white:box=1:boxcolor=0xC62C2C:boxborderw=14:x=625:y=1540:enable='gte(t,4.0)',\
drawtext=$DT:textfile=$TMP/t3.txt:fontsize=60:y=1700:enable='gte(t,2.0)'" \
  -an -c:v libx264 -pix_fmt yuv420p "$TMP/seg1.mp4"

# 2) reference beat 5-10.5s — reused from job-004 (Panchayat still, no credit bar)
ffmpeg -y -v error -ss 5 -i productions/job-20261023-004/out/final.mp4 -t 5.5 -an -c:v libx264 -pix_fmt yuv420p "$TMP/seg2.mp4"

# 3) closer 10.5-13.5s — empty wallet (stock), centre-cropped vertical
ffmpeg -y -v error -ss 2 -i library/clips/clip-20261023-008/clip.mp4 -t 3 \
  -vf "scale=-2:$H,crop=$W:$H,fps=$FPS,\
drawtext=$DT:textfile=$TMP/t4.txt:fontsize=94:y=120,\
drawtext=$DT:textfile=$TMP/t5.txt:fontsize=82:fontcolor=0xE33E3E:y=240,\
drawtext=$DT:textfile=$TMP/t6.txt:fontsize=54:y=1700" \
  -an -c:v libx264 -pix_fmt yuv420p "$TMP/seg3.mp4"

# 4) end card 13.5-17s — plain text card, no character
ffmpeg -y -v error -f lavfi -i "color=c=0x12162C:s=${W}x${H}:d=3.5:r=$FPS" \
  -vf "drawtext=fontfile=$FONT:textfile=$TMP/t7.txt:fontsize=150:fontcolor=0xF5B018:x=(w-text_w)/2:y=700,\
drawtext=fontfile=$FONT:textfile=$TMP/t8.txt:fontsize=58:fontcolor=white:x=(w-text_w)/2:y=920" \
  -c:v libx264 -pix_fmt yuv420p "$TMP/seg4.mp4"

# concat + the pilot's existing synth bed
printf "file 'seg1.mp4'\nfile 'seg2.mp4'\nfile 'seg3.mp4'\nfile 'seg4.mp4'\n" > "$TMP/list.txt"
ffmpeg -y -v error -f concat -safe 0 -i "$TMP/list.txt" -i productions/job-20261023-004/out/audio.wav \
  -c:v copy -c:a aac -shortest "$JOB/out/final.mp4"
rm -rf "$TMP"
echo "built $JOB/out/final.mp4"
