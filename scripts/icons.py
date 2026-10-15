"""Génère les icônes de l'app (web et Android). Lancer : python3 scripts/icons.py"""
import os
from PIL import Image, ImageDraw

BLUE = (47, 85, 212)
BG = (238, 241, 246)


def draw(size, pad, transparent=False, circle=False):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0) if transparent or circle else BLUE + (255,))
    d = ImageDraw.Draw(im)
    if circle:
        d.ellipse([0, 0, S - 1, S - 1], fill=BLUE + (255,))
    p = int(S * pad)
    x0, x1 = p, S - p
    w = x1 - x0
    y0 = int(S * 0.5 - w * 0.31)
    y1 = int(S * 0.5 + w * 0.19)
    h = y1 - y0
    d.rounded_rectangle([x0, y0, x1, y1], radius=int(w * 0.09), fill=(255, 255, 255, 255))
    pts = [(x0 + w * 0.10, y0 + h * 0.72), (x0 + w * 0.32, y0 + h * 0.48), (x0 + w * 0.52, y0 + h * 0.60), (x0 + w * 0.88, y0 + h * 0.24)]
    d.line(pts, fill=BLUE + (255,), width=int(w * 0.055), joint="curve")
    r = int(w * 0.045)
    ex, ey = pts[-1]
    d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=BLUE + (255,))
    by = y1 + int(w * 0.08)
    d.rounded_rectangle([x0, by, x0 + int(w * 0.45), by + int(w * 0.06)], radius=int(w * 0.03), fill=(255, 255, 255, 170))
    im = im.resize((size, size), Image.LANCZOS)
    return im if (transparent or circle) else im.convert("RGB")


def save(im, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path)


# Web
save(draw(192, 0.18), "icons/icon-192.png")
save(draw(512, 0.18), "icons/icon-512.png")
save(draw(512, 0.26), "icons/icon-maskable-512.png")
save(draw(180, 0.18), "icons/apple-touch-icon.png")

# Android : copiées par-dessus le projet généré par Capacitor
res = "android-res"
for dpi, legacy, fg in [("mdpi", 48, 108), ("hdpi", 72, 162), ("xhdpi", 96, 216), ("xxhdpi", 144, 324), ("xxxhdpi", 192, 432)]:
    save(draw(legacy, 0.18), f"{res}/mipmap-{dpi}/ic_launcher.png")
    save(draw(legacy, 0.20, circle=True), f"{res}/mipmap-{dpi}/ic_launcher_round.png")
    save(draw(fg, 0.30, transparent=True), f"{res}/mipmap-{dpi}/ic_launcher_foreground.png")
save(Image.new("RGB", (64, 64), BG), f"{res}/drawable/splash.png")
os.makedirs(f"{res}/values", exist_ok=True)
with open(f"{res}/values/ic_launcher_background.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#2F55D4</color>\n</resources>\n')
