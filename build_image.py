#!/usr/bin/env python3
"""Build the news-image-20261123 front page deterministically with PIL.
1024x1024, newspaper front-page style. All text from the verified list
supplied in the task; no invented dates, numbers or quotes.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
GREY = (90, 86, 78)
RED = (180, 35, 24)
NAVY = (18, 38, 66)
TEAL = (14, 90, 90)
BLUE = (29, 78, 137)
AMBER = (176, 106, 0)
GREEN = (34, 110, 72)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning list of lines fitting max_w."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, fnt, max_w, fill=INK, leading=1.25):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36  # margin
X1 = W - M

# ---- Masthead ----
d.text((M, 22), "THE WORLD TODAY", font=font(SERIF_B, 62), fill=INK)
d.text((M, 96), "MONDAY, 23 NOVEMBER 2026  •  THE DAY'S WORLD NEWS, IN ONE PAGE",
       font=font(SANS_B, 21), fill=RED)
d.line([(M, 138), (X1, 138)], fill=INK, width=4)
d.line([(M, 144), (X1, 144)], fill=INK, width=1)

# ---- Lead story ----
y = 162
d.rectangle([(M, y), (M + 230, y + 30)], fill=RED)
d.text((M + 12, y + 4), "LEAD  •  CLIMATE", font=font(SANS_B, 20), fill=(255, 255, 255))
lead_x = M
lead_w = 600
y = 208
y = draw_wrapped(d, lead_x, y, "COP31 climate deal\ncollapses", font(SERIF_B, 52), lead_w, leading=1.08)
y += 8
y = draw_wrapped(d, lead_x, y,
    "Nearly 200 countries fail to agree a climate declaration as COP31 ends in chaos. UN chief: \u2018no ambiguity in the science\u2019.",
    font(SANS, 23), lead_w, leading=1.3)

# Lead graphic panel (right)
gx, gy, gw, gh = 668, 162, 320, 268
d.rectangle([(gx, gy), (gx + gw, gy + gh)], fill=NAVY)
# globe
cx, cy, r = gx + 160, gy + 92, 68
d.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(64, 130, 190), outline=(255, 255, 255), width=3)
d.ellipse([(cx - 52, cy - 48), (cx + 8, cy + 2)], fill=(74, 160, 90))
d.ellipse([(cx - 6, cy + 18), (cx + 58, cy + 62)], fill=(74, 160, 90))
# crack across globe
d.line([(cx - 70, cy - 60), (cx - 30, cy - 10), (cx - 52, cy + 28), (cx - 8, cy + 66), (cx + 18, cy + 30)],
       fill=(255, 90, 60), width=6)
d.text((gx + 16, gy + gh - 38), "COP31  •  NO DEAL", font=font(SANS_B, 24), fill=(255, 255, 255))
d.text((gx + 16, gy + 178), "Nearly 200 nations,", font=font(SANS, 20), fill=(210, 220, 235))
d.text((gx + 16, gy + 202), "no agreement.", font=font(SANS, 20), fill=(210, 220, 235))

d.line([(M, 452), (X1, 452)], fill=INK, width=2)

# ---- Grid: 6 stories, 2 cols x 3 rows ----
stories = [
    ("US", BLUE, "Democrats clinch historic\nUS House majority",
     "At least 258 seats \u2014 the largest Democratic majority since 1992."),
    ("IRAN", RED, "Iran and US on edge over\n\u2018neither war nor peace\u2019",
     "Tehran seeks a \u2018clear and operational\u2019 path; tankers struck in the Strait of Hormuz."),
    ("UKRAINE", NAVY, "Russian strikes kill 11\nin Kyiv region",
     "Deadly overnight attacks hit the region around Ukraine\u2019s capital."),
    ("N. KOREA", TEAL, "Kim: North Korea seeks\nsecurity, not supremacy",
     "Pyongyang says its goal is security, not dominance."),
    ("MEXICO", GREEN, "FBI-wanted cartel leader\ncaptured in Sinaloa",
     "Chapo Isidro arrested in a major operation in Mexico."),
    ("INDONESIA", AMBER, "Factory fire kills 3;\n36 missing",
     "Rescuers search for dozens missing after the blaze in Indonesia."),
]
gx0, gy0 = M, 472
cell_w, cell_h = 466, 138
col_gap, row_gap = 20, 12
for i, (tag, colour, head, summ) in enumerate(stories):
    cx0 = gx0 + (i % 2) * (cell_w + col_gap)
    cy0 = gy0 + (i // 2) * (cell_h + row_gap)
    d.rectangle([(cx0, cy0), (cx0 + cell_w, cy0 + cell_h)], outline=(180, 174, 162), width=1)
    tag_w = int(d.textlength(tag, font=font(SANS_B, 18))) + 18
    d.rectangle([(cx0, cy0), (cx0 + tag_w, cy0 + 28)], fill=colour)
    d.text((cx0 + 8, cy0 + 4), tag, font=font(SANS_B, 18), fill=(255, 255, 255))
    ty = cy0 + 36
    ty = draw_wrapped(d, cx0 + 12, ty, head, font(SERIF_B, 25), cell_w - 24, leading=1.08)
    draw_wrapped(d, cx0 + 12, ty + 2, summ, font(SANS, 19), cell_w - 24, fill=GREY, leading=1.22)

# ---- Footer: also today ----
fy = 472 + 3 * cell_h + 2 * row_gap + 14
d.line([(M, fy), (X1, fy)], fill=INK, width=2)
d.text((M, fy + 10), "ALSO TODAY", font=font(SANS_B, 20), fill=RED)
items = [
    "S. Korea education chief quits in AI cheating scandal.",
    "Trump backs Jensen Huang\u2019s Nvidia rehire.",
    "US rushes to shield air traffic before Thanksgiving.",
    "BepiColombo spacecraft reaches Mercury.",
]
iy = fy + 42
for j, it in enumerate(items):
    ix = M + (j % 2) * 476
    iy2 = iy + (j // 2) * 30
    d.text((ix, iy2), "\u2022  " + it, font=font(SANS, 17), fill=INK)

img.save("/home/hatch/workspace/makefun-news-image/work/entry.png", "PNG", optimize=True)
print("saved")
