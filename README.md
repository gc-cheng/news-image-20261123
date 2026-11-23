# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/gc-cheng/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/gc-cheng/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

The World Today — Monday, 23 November 2026. make.fun bounty entry for **news-image-20261123**: sum up the world's news of Monday 23 November 2026 in one image.

The entry is a 1024×1024 newspaper front page, **THE WORLD TODAY**, drawn with Python/PIL (`build_image.py`, included here) from the verified news of the day:

- **Lead — COP31 climate deal collapses:** nearly 200 countries fail to agree on a climate declaration as COP31 ends in chaos; the UN chief warns there is "no ambiguity in the science".
- **US:** Democrats clinch a historic House majority of at least 258 seats, the largest since 1992.
- **Iran/US:** Tehran seeks a "clear and operational" path out of "neither war nor peace"; tankers struck in the Strait of Hormuz.
- **Ukraine:** Russian strikes kill 11 in the Kyiv region.
- **North Korea:** Kim says the country seeks security, not supremacy.
- **Mexico:** FBI-wanted cartel leader Chapo Isidro captured in Sinaloa.
- **Indonesia:** factory fire kills 3, with 36 missing.
- **Also today:** South Korea's education chief quits amid an AI cheating scandal; Trump backs Jensen Huang's Nvidia rehire; the US rushes to shield air traffic before Thanksgiving; BepiColombo reaches Mercury.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the image stored as `entry.png` in this repo and writes it to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` outside the grader). No network, no timestamps, no randomness — two runs write byte-identical output. The image was drawn with Python/PIL by `build_image.py`, included here for provenance.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=3pf76s6q&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
