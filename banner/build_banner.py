#!/usr/bin/env python3
"""Banner homenaje a Enrique "Gato" Piedfort  —  85 x 200 cm.
Salida: SVG vectorial editable (tamano real) + PNG de vista previa.
Solo requiere Pillow.  Correr desde la raiz del repo:  python3 banner/build_banner.py
"""
import base64, io, re, html
from pathlib import Path
from PIL import Image, ImageFilter, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT / "banner"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- lienzo (mm)
W, H = 850, 2000
MX   = 60

# ---------------------------------------------------------------- paleta (= web)
DEEP, DEEP2, DEEP3 = "#04263A", "#072f47", "#021a29"
POOL, SHALLOW      = "#0B6E8F", "#3FC1C9"
GOLD               = "#E8B04B"

# ---------------------------------------------------------------- geometria
PHOTO_H   = 962                      # franja superior, ancho completo
NAME_Y    = (1142, 1254, 1396)       # baselines ENRIQUE / "GATO" / PIEDFORT
DATES_Y   = 1482
ROPE2_Y   = 1520
PHRASE_Y0 = 1588
PHRASE_LH = 48
ROPE3_Y   = 1720
QR_CARD_Y = 1748
QR_CARD   = 224
QR_PAD    = 20
QR_TX     = MX + QR_CARD + 42

PHRASE_LINES = [
    "Jugador, entrenador y formador",
    "de generaciones enteras.",
    ("Una leyenda de nuestro deporte.", None),   # linea en dorado
]
QR_LINES = ["Conocé su historia", "escaneando el QR."]

def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- foto (embebida)
src = Image.open(ROOT / "img" / "gato_profile.png").convert("RGB")
scale = 2
big = src.resize((src.width*scale, src.height*scale), Image.LANCZOS)
big = big.filter(ImageFilter.UnsharpMask(radius=2.2, percent=90, threshold=2))
buf = io.BytesIO()
big.save(buf, "JPEG", quality=90, optimize=True, progressive=True)
photo_b64 = base64.b64encode(buf.getvalue()).decode()
print(f"foto embebida: {big.width}x{big.height}px  {len(buf.getvalue())/1024:.0f} KB")

# ---------------------------------------------------------------- QR (vector)
qr_raw = (ROOT / "assets" / "qr" / "qr.svg").read_text()
qr_inner = re.sub(r"^.*?<svg[^>]*>(.*)</svg>\s*$", r"\1", qr_raw, flags=re.S).strip()

# ==================================================================  SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">
  <title>Enrique "Gato" Piedfort — banner homenaje 85 x 200 cm</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="{DEEP2}"/>
      <stop offset="0.5"  stop-color="{DEEP}"/>
      <stop offset="1"    stop-color="{DEEP3}"/>
    </linearGradient>
    <linearGradient id="photofade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="{DEEP}" stop-opacity="0"/>
      <stop offset="0.72" stop-color="{DEEP}" stop-opacity="0"/>
      <stop offset="1"    stop-color="{DEEP}" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="phototop" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"   stop-color="{DEEP3}" stop-opacity="0.62"/>
      <stop offset="1"   stop-color="{DEEP3}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="waterline" gradientUnits="userSpaceOnUse"
        x1="0" y1="1030" x2="0" y2="1400">
      <stop offset="0"    stop-color="#ffffff"/>
      <stop offset="0.72" stop-color="#eafcff"/>
      <stop offset="0.75" stop-color="{SHALLOW}"/>
      <stop offset="1"    stop-color="#7ad3d9"/>
    </linearGradient>
    <radialGradient id="caustic1" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0"    stop-color="{SHALLOW}" stop-opacity="0.45"/>
      <stop offset="0.62" stop-color="{SHALLOW}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="caustic2" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0"   stop-color="{POOL}" stop-opacity="0.5"/>
      <stop offset="0.6" stop-color="{POOL}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="rope" width="64" height="12" patternUnits="userSpaceOnUse">
      <rect width="64" height="12" fill="{DEEP}"/>
      <rect width="16" height="12" x="0"  fill="{GOLD}"/>
      <rect width="8"  height="12" x="16" fill="#f4f6f7"/>
      <rect width="16" height="12" x="24" fill="{POOL}"/>
      <rect width="8"  height="12" x="40" fill="#f4f6f7"/>
      <rect width="16" height="12" x="48" fill="{GOLD}"/>
    </pattern>
    <clipPath id="photoclip"><rect x="0" y="0" width="{W}" height="{PHOTO_H}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <ellipse cx="770" cy="1360" rx="640" ry="640" fill="url(#caustic2)"/>
  <ellipse cx="90"  cy="1720" rx="480" ry="480" fill="url(#caustic1)"/>

  <!-- ================================================= foto (arriba, ancho completo) -->
  <g clip-path="url(#photoclip)">
    <image x="0" y="0" width="{W}" height="{round(W*src.height/src.width)}"
           preserveAspectRatio="xMidYMin slice"
           xlink:href="data:image/jpeg;base64,{photo_b64}"/>
    <rect x="0" y="0" width="{W}" height="{PHOTO_H}" fill="url(#photofade)"/>
    <rect x="0" y="0" width="{W}" height="150" fill="url(#phototop)"/>
  </g>
  <rect x="{MX}" y="26" width="26" height="3" fill="{GOLD}"/>
  <text x="{MX+40}" y="32" fill="#ffffff"
        font-family="'Barlow','Barlow Condensed','Arial Narrow',sans-serif"
        font-size="15" font-weight="600" letter-spacing="4.2">H O M E N A J E</text>
  <rect x="{MX}" y="{PHOTO_H-6}" width="{W-2*MX}" height="12" fill="url(#rope)"/>

  <!-- ================================================= nombre -->
  <g font-family="'Anton','Barlow Condensed','Arial Narrow Bold',sans-serif" letter-spacing="1">
    <text x="{MX-3}" y="{NAME_Y[0]}" font-size="150" fill="url(#waterline)">ENRIQUE</text>
    <text x="{MX-3}" y="{NAME_Y[1]}" font-size="92"  fill="{GOLD}">&#8220;GATO&#8221;</text>
    <text x="{MX-3}" y="{NAME_Y[2]}" font-size="150" fill="url(#waterline)">PIEDFORT</text>
  </g>

  <!-- fechas 1945 - infinito -->
  <g font-family="'Barlow','Arial Narrow',sans-serif">
    <text x="{MX-1}" y="{DATES_Y}" font-size="46" font-weight="600" fill="{GOLD}"
          letter-spacing="2">1945</text>
    <rect x="{MX+120}" y="{DATES_Y-18}" width="34" height="4" fill="{GOLD}"/>
    <path fill="none" stroke="{GOLD}" stroke-width="7"
          transform="translate({MX+205},{DATES_Y-16})"
          d="M0,0 C -6,-14 -24,-14 -24,0 C -24,14 -6,14 0,0 C 6,-14 24,-14 24,0 C 24,14 6,14 0,0 Z"/>
  </g>

  <rect x="{MX}" y="{ROPE2_Y}" width="{W-2*MX}" height="12" fill="url(#rope)"/>

  <!-- ================================================= frase -->
  <g font-family="'Source Serif 4','Source Serif Pro',Georgia,serif"
     font-style="italic" text-anchor="middle" font-size="33">
'''
py = PHRASE_Y0
for ln in PHRASE_LINES:
    txt = ln[0] if isinstance(ln, tuple) else ln
    fill = GOLD if isinstance(ln, tuple) else "#ffffff"
    op   = "" if isinstance(ln, tuple) else ' fill-opacity="0.92"'
    svg += f'    <text x="{W/2}" y="{py}" fill="{fill}"{op}>{esc(txt)}</text>\n'
    py += PHRASE_LH

svg += f'''  </g>

  <rect x="{MX}" y="{ROPE3_Y}" width="{W-2*MX}" height="12" fill="url(#rope)"/>

  <!-- ================================================= QR -->
  <rect x="{MX}" y="{QR_CARD_Y}" width="{QR_CARD}" height="{QR_CARD}" rx="6"
        fill="#ffffff" stroke="{POOL}" stroke-opacity="0.25"/>
  <svg x="{MX+QR_PAD}" y="{QR_CARD_Y+QR_PAD}" width="{QR_CARD-2*QR_PAD}"
       height="{QR_CARD-2*QR_PAD}" viewBox="0 0 410 410">{qr_inner}</svg>
  <g font-family="'Source Serif 4','Source Serif Pro',Georgia,serif"
     font-size="34" fill="#ffffff" fill-opacity="0.92">
    <text x="{QR_TX}" y="{QR_CARD_Y + QR_CARD/2 - 6}">{esc(QR_LINES[0])}</text>
    <text x="{QR_TX}" y="{QR_CARD_Y + QR_CARD/2 + 40}">{esc(QR_LINES[1])}</text>
  </g>
</svg>
'''
svg_path = OUT / "banner-gato-piedfort-85x200.svg"
svg_path.write_text(svg)
print(f"SVG: {svg_path.name}  {len(svg)/1024:.0f} KB")

# ==================================================================  VISTA PREVIA
PX = 1.5
cw, ch = round(W*PX), round(H*PX)
def mm(v): return round(v*PX)
def hx(c):
    c = c.lstrip("#"); return tuple(int(c[i:i+2],16) for i in (0,2,4))

img = Image.new("RGB", (cw, ch), DEEP)
d = ImageDraw.Draw(img, "RGBA")

# fondo degradado
top, mid, bot = hx(DEEP2), hx(DEEP), hx(DEEP3)
for y in range(ch):
    t = y/ch
    if t < 0.5:
        k = t/0.5;  col = tuple(round(top[i]+(mid[i]-top[i])*k) for i in range(3))
    else:
        k = (t-0.5)/0.5; col = tuple(round(mid[i]+(bot[i]-mid[i])*k) for i in range(3))
    d.line([(0,y),(cw,y)], fill=col)

def blob(cx, cy, r, col, a):
    layer = Image.new("RGBA", (cw, ch), (0,0,0,0))
    ImageDraw.Draw(layer).ellipse([cx-r,cy-r,cx+r,cy+r], fill=col+(a,))
    layer = layer.filter(ImageFilter.GaussianBlur(r*0.35))
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"), (0,0))
blob(770*PX,1360*PX, 640*PX, hx(POOL), 55)
blob(90*PX, 1720*PX, 480*PX, hx(SHALLOW), 40)
d = ImageDraw.Draw(img, "RGBA")

F = "/usr/share/fonts/opentype/urw-base35/"
def font(name, s): return ImageFont.truetype(F+name, round(s*PX))
disp   = lambda s: font("NimbusSansNarrow-Bold.otf", s)
serif  = lambda s: font("NimbusRoman-Italic.otf", s)
util   = lambda s: font("NimbusSansNarrow-Bold.otf", s)

def T(x, y, s, f, fill, ls=0):
    cx = x
    for chn in s:
        d.text((cx, y), chn, font=f, fill=fill, anchor="ls")
        cx += d.textlength(chn, font=f) + ls*PX

# foto arriba (ancho completo, recorte desde arriba)
ph_full = src.resize((cw, round(cw*src.height/src.width)), Image.LANCZOS)
img.paste(ph_full.crop((0, 0, cw, mm(PHOTO_H))), (0, 0))
fade = Image.new("RGBA", (cw, mm(PHOTO_H)), (0,0,0,0))
fd = ImageDraw.Draw(fade)
dc = hx(DEEP)
d3 = hx(DEEP3)
toph = mm(150)
for y in range(mm(PHOTO_H)):
    t = y/mm(PHOTO_H)
    a = 0 if t < 0.72 else round(255*(t-0.72)/0.28)
    fd.line([(0,y),(cw,y)], fill=dc+(a,))
    if y < toph:
        at = round(158*(1 - y/toph))
        fd.line([(0,y),(cw,y)], fill=d3+(max(at, a),))
img.paste(fade, (0,0), fade)
d = ImageDraw.Draw(img, "RGBA")

d.rectangle([mm(MX), mm(26), mm(MX+26), mm(29)], fill=hx(GOLD))
T(mm(MX+40), mm(33), "HOMENAJE", util(15), (255,255,255,255), ls=6)

def rope(y):
    seg, x, i = 8, mm(MX), 0
    cols = [GOLD, "#f4f6f7", POOL, "#f4f6f7", GOLD, DEEP, DEEP, DEEP]
    while x < mm(W-MX):
        d.rectangle([x, mm(y), x+mm(seg), mm(y+12)], fill=hx(cols[i%8]))
        x += mm(seg); i += 1
rope(PHOTO_H-6)

# nombre con waterline
def waterline_text(x, baseline, s, size):
    f = disp(size)
    msk = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(msk).text((x, baseline), s, font=f, fill=255, anchor="ls")
    grad = Image.new("RGB", (cw, ch)); gd = ImageDraw.Draw(grad)
    y0, y1 = mm(1030), mm(1400)
    w1, w2 = hx(SHALLOW), hx("#7ad3d9")
    for y in range(ch):
        if y <= y0 + (y1-y0)*0.73: col = (255,255,255)
        elif y >= y1: col = w2
        else:
            kk = (y - (y0+(y1-y0)*0.73)) / max(1,(y1-(y0+(y1-y0)*0.73)))
            col = tuple(round(w1[i]+(w2[i]-w1[i])*kk) for i in range(3))
        gd.line([(0,y),(cw,y)], fill=col)
    img.paste(grad, (0,0), msk)

waterline_text(mm(MX-3), mm(NAME_Y[0]), "ENRIQUE", 150)
T(mm(MX-3), mm(NAME_Y[1]), "“GATO”", disp(92), hx(GOLD))
waterline_text(mm(MX-3), mm(NAME_Y[2]), "PIEDFORT", 150)
d = ImageDraw.Draw(img, "RGBA")

# fechas
T(mm(MX-1), mm(DATES_Y), "1945", util(46), hx(GOLD), ls=2)
d.rectangle([mm(MX+120), mm(DATES_Y-18), mm(MX+154), mm(DATES_Y-14)], fill=hx(GOLD))
for dxc in (-12, 12):
    d.ellipse([mm(MX+205+dxc-13), mm(DATES_Y-16-13), mm(MX+205+dxc+13), mm(DATES_Y-16+13)],
              outline=hx(GOLD), width=mm(7))
rope(ROPE2_Y)

# frase
py = PHRASE_Y0
for ln in PHRASE_LINES:
    txt = ln[0] if isinstance(ln, tuple) else ln
    fill = hx(GOLD) if isinstance(ln, tuple) else (255,255,255,235)
    d.text((cw/2, mm(py)), txt, font=serif(33), fill=fill, anchor="ms")
    py += PHRASE_LH
rope(ROPE3_Y)

# QR
qy, qc, qp = mm(QR_CARD_Y), mm(QR_CARD), mm(QR_PAD)
d.rounded_rectangle([mm(MX), qy, mm(MX)+qc, qy+qc], radius=mm(6), fill=(255,255,255))
qim = Image.open(ROOT/"assets"/"qr"/"qr.png").convert("L").resize((qc-2*qp, qc-2*qp), Image.NEAREST)
img.paste(qim.convert("RGB"), (mm(MX)+qp, qy+qp))
d.text((mm(QR_TX), qy+qc/2 - mm(6)),  QR_LINES[0], font=serif(34), fill=(255,255,255,235), anchor="ls")
d.text((mm(QR_TX), qy+qc/2 + mm(40)), QR_LINES[1], font=serif(34), fill=(255,255,255,235), anchor="ls")

prev_path = OUT / "banner-gato-piedfort-85x200-preview.png"
img.save(prev_path, optimize=True)
print(f"preview: {prev_path.name}  {img.size}")
