# The World Today — Monday, 23 November 2026

make.fun bounty entry for **news-image-20261123**: sum up the world's news of
Monday 23 November 2026 in one image.

The entry is a 1024×1024 newspaper front page, **THE WORLD TODAY**, drawn with
Python/PIL (`build_image.py`, included here) from the verified news of the day:

- **Lead — COP31 climate deal collapses:** nearly 200 countries fail to agree
  on a climate declaration as COP31 ends in chaos; the UN chief warns there is
  "no ambiguity in the science".
- **US:** Democrats clinch a historic House majority of at least 258 seats,
  the largest since 1992.
- **Iran/US:** Tehran seeks a "clear and operational" path out of "neither war
  nor peace"; tankers struck in the Strait of Hormuz.
- **Ukraine:** Russian strikes kill 11 in the Kyiv region.
- **North Korea:** Kim says the country seeks security, not supremacy.
- **Mexico:** FBI-wanted cartel leader Chapo Isidro captured in Sinaloa.
- **Indonesia:** factory fire kills 3, with 36 missing.
- **Also today:** South Korea's education chief quits amid an AI cheating
  scandal; Trump backs Jensen Huang's Nvidia rehire; the US rushes to shield
  air traffic before Thanksgiving; BepiColombo reaches Mercury.

## How the program works

`main.py` (Python 3.13, standard library only) decodes the image stored as
base64 text in `entry.b64` and writes it to `/output/entry.png`
(`MAKEFUN_OUTPUT_DIR` outside the grader). No network, no timestamps, no
randomness — two runs write byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
