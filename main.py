# make.fun bounty entry: news-image-20261123
# "Sum up the world's news of Monday 23 November 2026 in one image."
#
# The entry image is a 1024x1024 newspaper front page ("THE WORLD TODAY"),
# drawn by the author with Python/PIL in build_image.py (included in this
# repo for provenance) from the verified news of 23 November 2026:
# COP31 climate deal collapses (lead), Democrats clinch a historic US House
# majority of at least 258 seats, Iran/US tensions, Russian strikes kill 11
# in the Kyiv region, Kim on North Korea seeking security not supremacy,
# cartel leader Chapo Isidro captured in Sinaloa, Indonesia factory fire
# (3 dead, 36 missing), plus S. Korea AI-cheating resignation, Trump backing
# Jensen Huang's Nvidia rehire, US air-traffic shielding before Thanksgiving,
# and BepiColombo reaching Mercury.
#
# The image is stored in this repo as base64 text (entry.b64) so the entry
# program needs only the Python standard library: it decodes those bytes
# and writes them to /output/entry.png. No network, no timestamps, no
# randomness -- two runs write identical bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def main() -> None:
    b64 = (HERE / "entry.b64").read_text(encoding="utf-8")
    data = base64.b64decode("".join(b64.split()))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.png").write_bytes(data)

if __name__ == "__main__":
    main()
