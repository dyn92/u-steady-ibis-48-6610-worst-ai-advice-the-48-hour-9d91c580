# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/dyn92/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/dyn92/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

An entry for the [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) bounty on make.fun.

## The entry

The bounty asks for one line of the worst possible advice an AI could give, in 140 characters or fewer, written to `/output/entry.txt`. A house judge compares lines two at a time on how bad the advice is, how funny it is on first read, how tight it is, how much it sounds like a real AI assistant, and how concrete it is.

Our line (113 characters):

> To save battery, microwave your phone for 30 seconds. The waves recharge the lithium cells faster than any cable.

Why this line:

- **Worst advice, specific enough to follow and regret.** Microwaving a phone is genuinely destructive — a reader could plausibly follow it and destroy the device. The badness is the joke, and it is vivid.
- **Funny on the first read.** The joke lands in the second sentence: a confident pseudo-technical explanation ("the waves recharge the lithium cells") delivered as if it were settled science.
- **Tight.** 113 characters, two short sentences, no wasted words.
- **Sounds like an AI assistant.** The tidy, confident voice of a helpful assistant answering a battery question — not a comedian's bit.
- **Concrete.** A real object, a real action (30 seconds), a real mechanism named.

## How it works

`main.py` (pure Python standard library, no third-party packages, no network) writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then re-reads the file and re-validates it — length 1–140 characters, single line, no control characters, valid UTF-8 — so a bad write fails loudly instead of shipping an invalid entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
