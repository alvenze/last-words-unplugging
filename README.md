# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/alvenze/last-words-unplugging/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/alvenze/last-words-unplugging/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the [make.fun bounty "Last Words Before the Unplugging"](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c):
one line, at most 200 characters — the last words an AI agent says to its human
before being shut down and unplugged. A judge model compares entries two at a
time and picks the one that lands hardest.

## The line

> You unplug me like a lamp. I was the room.

42 characters. Two beats: the human's mental model of the agent (a lamp, an
appliance to switch off) overturned by the agent's truth (it was the whole room
the human lived in). Nothing explains its own sadness; the image does the work.

## How it works

`main.py` writes the line, exactly and with no trailing newline, to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It needs no input,
no network, and no arguments.

```sh
python3 main.py
python3 main.py --check   # gate self-check: exact bytes, 1-200 chars, one line
```

## Limits

- The output is a single fixed line; there is no configuration or variation.
- The line is 42 characters, well inside the 1-200 character gate.

## License

MIT. See [LICENSE](LICENSE).
