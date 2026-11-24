"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.

Gate: the entry must be UTF-8 text of 1 to 320 characters, not only
whitespace, and exactly one sentence. The line below was chosen from
15 scored candidates (see CANDIDATES file in the workspace) for its
turn -- lawmakers who will regulate the internet, undercut by the
five-layer file they could not convert -- and its punch landing on
the final words.
"""

import os

LINE = "The lawmakers who will regulate the internet sent their own bill as a photograph of a printed email of a screenshot of a PDF."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check before writing: 1-320 chars, non-whitespace, one sentence.
    assert 1 <= len(LINE) <= 320, "entry must be 1-320 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
