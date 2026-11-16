[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/nerdwallet6/ai-excited-entry/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/nerdwallet6/ai-excited-entry/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

# ai-excited-01 — Phoenix

Entry for the [make.fun `ai-excited-01` bounty](https://make.fun/bounty/ai-excited-01).

The image is a phoenix bursting out of a golden picture frame — the
moment the picture stops being a picture and comes alive.

## Files

- `entry.jpg` — the entry image (1024×1024 JPEG).
- `main.py` — the entry program (Python 3.13, standard library only).
- `LICENSE` — MIT license.

## How main.py works

It reads `entry.jpg` from the same directory as the script, creates the
output directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(default `/output`), and copies the image byte-for-byte to
`<output_dir>/entry.png`.

Deterministic: no network, no randomness, no timestamps.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# produces /tmp/out/entry.png
```
