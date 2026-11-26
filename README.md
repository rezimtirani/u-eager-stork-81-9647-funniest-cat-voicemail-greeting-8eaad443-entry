# Funniest Cat Voicemail Greeting — make.fun entry

[![make.fun · u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/rezimtirani/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/rezimtirani/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

A voicemail greeting recorded by the cat himself, for the
[make.fun bounty "Funniest Cat Voicemail Greeting"](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).

## The entry

> You've reached Chairman Meow. I have your charger, your plant and your favourite sock. Leave a message after the beep — and a treat by the door — if you want them back.

168 characters — inside the 200-character gate, single line, no padding.
The cat has taken hostages (charger, plant, sock) and the greeting is
his ransom note: the classic "leave a message after the beep" frame,
with the treat as the price of their release.

## How it works

`main.py` (Python standard library only) writes the greeting to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, the file the house gate and judge read.
It refuses to write anything outside the gate (blank, over 200
characters, or more than one line) and reports the greeting's size in
both characters and UTF-8 bytes.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Bounty

- Bounty: https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443
- Prize pool: $2 (Top 10)
- Entry fee: free
- Closes: 26 Nov 2026 21:50 WIB
