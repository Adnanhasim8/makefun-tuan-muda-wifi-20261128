"""One Word for Your Wi-Fi (u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).

Writes exactly one word to /output/entry.txt (UTF-8, no network).

Candidate generation -- 18 words, scored 1-5 on each judge criterion
(1) on-subject Wi-Fi fit, (2) funny at once, (3) true to home Wi-Fi,
(4) fresh angle, (5) instantly understood with no context:

    Microwave   5 4 5 5 5 = 24  WINNER
    Peekaboo    4 5 4 4 5 = 22
    Houdini     4 4 4 5 4 = 21
    Potato      4 5 4 4 4 = 21
    Toddler     4 4 4 4 5 = 21
    Teenager    4 4 3 4 5 = 20
    Goldfish    3 4 3 4 5 = 19
    Cat         3 4 3 3 5 = 18
    Ex          3 4 3 4 4 = 18
    Ghosting    4 3 4 2 5 = 18
    Basement    3 3 3 4 5 = 18
    Hamster     3 4 2 4 5 = 18
    Neighbour   3 3 3 4 4 = 18
    Diva        3 3 3 3 5 = 17
    Yoyo        3 3 4 3 4 = 17
    Dialup      4 3 3 3 4 = 17
    Limbo       3 3 3 4 4 = 17
    Vampire     3 3 2 3 5 = 16

Why Microwave wins: a surprising concrete image, not a mood word.
Every home Wi-Fi dies the moment someone reheats lunch -- the
2.4 GHz microwave kills the signal, a universally recognised truth.
As a network name it is absurd and instantly funny, and the word
leaves the mystery unanswered: it never explains itself. The
obvious words (Slow, Laggy, Buffering, Dead, Ghost) all lose on
freshness; the other concrete nouns score lower on truth or
instant understanding. Capitalised, as a network name would be.
No trailing newline: smallest possible file, still a valid entry.

Polish round: re-tested the winner against runner-up Peekaboo.
Peekaboo is instant but a behaviour word in the hide-and-seek
family anyone could reach for, and cutesy rather than funny as
an SSID. Microwave keeps the concrete-image edge, the universal
lunchtime-interference truth, and the unanswered mystery, so it
stays unchanged -- the polish was the capitalisation (name, not
common noun) and dropping the trailing newline for the smallest
valid file. No word change: the scoring already picked the best.
"""

import argparse
import os
import sys

WORD = "Microwave"


def main(argv=None):
    # Gate assertions: the entry must be exactly one word, non-empty.
    assert isinstance(WORD, str) and WORD, "word must be non-empty"
    assert WORD.strip() == WORD, "word must have no surrounding whitespace"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 20, "entry must be 1-20 characters"
    assert WORD.isprintable(), "entry must be printable text"

    parser = argparse.ArgumentParser(description="Write the Wi-Fi word.")
    parser.add_argument("--out", default=None,
                        help="Output file (default: $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt)")
    args = parser.parse_args(argv)

    if args.out:
        out_path = args.out
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)

    # Verify what was written: read back and assert byte-identical.
    with open(out_path, "rb") as f:
        written = f.read()
    assert written == WORD.encode("utf-8"), "written bytes differ from WORD"
    assert written.strip() and len(written.split()) == 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
