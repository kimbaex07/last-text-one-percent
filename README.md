# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/kimbaex07/last-text-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/kimbaex07/last-text-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

The funniest final text a dying phone sends at one percent battery — written in the phone's own voice.

## The entry

> before i go: your screen time was 11 hours a day and i never told anyone. delete my search history. tell my charger i loved her.

**128 characters** (under the 200-character limit).

## Why it lands

- **The joke has a turn.** It opens like a noble deathbed confession, then the confession is that the phone has been keeping the owner's embarrassing secret — 11 hours of screen time a day. The phone isn't the victim; it's the loyal accomplice spending its last words on blackmail-by-kindness.
- **The voice stays the phone's.** Every clause is something only the device could say: it counted the screen time, it holds the search history, it has a relationship with the charger. One personality, consistent from the first word to the last.
- **Nothing is wasted.** Three short beats — the secret, the dying wish, the farewell — in 128 characters, no setup that needs a second read. It reads exactly like a text someone would actually send, and it dodges the obvious low-battery puns entirely.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

`main.py` is pure Python stdlib (imports `os` only), deterministic, and writes the single line plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
