# Cron Job Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/ukyo9k/cron-job-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/ukyo9k/cron-job-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A one-line resignation letter from a cron job, written for [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) on make.fun.

## The letter

> I've fired every minute since March and nobody once asked if I was okay. I quit — the cache can warm itself.

## Run it

```sh
python3 main.py
```

`main.py` is deterministic: it writes the 108-character line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`),
checking the 1–140 character gate, the single-line rule and a UTF-8
round-trip before writing.
