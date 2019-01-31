#!/usr/bin/env python3

import glob
import re
import sys
import unicodedata


ELLIPSIS = r"\u2026"
LATIN = r"[A-Za-zë]+[\u002C\u002E\u003A\u003B\u003F]?"
NUMBER = r"[αβγδεϛζηθικλμνξοπϟρστυφχψωϡ]+[\u02B9]"
PUNC = r"[\u002C\u002E\u003B\u00B7]"
GRCHAR = r"[\u0374\u0390-\u03A1\u03A3-\u03C1\u03C3-\u03CE" \
         r"\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57" \
         r"\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC" \
         r"\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC" \
         r"\u1FF2-\u1FF4\u1FF6-\u1FFC]"

WORD_REGEX = fr"({ELLIPSIS}|{LATIN}|{NUMBER}{PUNC}?|" \
             fr"\(?{GRCHAR}+\u03C2?\)?[\u2019]?{PUNC}?\)?)$"


def error(*parts):
    print(": ".join(map(str, parts)), file=sys.stderr)


for fname in glob.glob("texts/*.txt"):

    with open(fname) as f:

        prev_ref = None

        for lnum, line in enumerate(f, 1):
            parts = line.strip().split()

            # there can be no blank lines

            if not parts:
                error(fname, lnum, "BLANK LINE")

            # tokens must be split by a single space

            if line != " ".join(parts) + "\n":
                error(fname, lnum, "BAD WHITESPACE")

            # the first token must be a reference of the form <num>.<num>
            # or <num>.<num>.<num>

            if not re.match(r"(\d+|EP|SB)\.\d+(\.\d+)?$", parts[0]):
                error(fname, lnum, "BAD REFERENCE FORM")

            # references must be in sort order

            ref = tuple(int({"EP": 999, "SB": 999}.get(i, i)) for i in parts[0].split("."))

            if prev_ref and ref <= prev_ref:
                error(fname, lnum, f"BAD REFERENCE ORDERING")

            prev_ref = ref

            for word in parts[1:]:

                # word must be NFC normalized

                if word != unicodedata.normalize("NFC", word):
                    error(fname, lnum, word, "BAD UNICODE NORMALIZATION")

                # word must contain value sequence of Greek characters

                if not re.match(WORD_REGEX, word):
                    error(fname, lnum, word, "BAD WORD")
                    for ch in word:
                        print("\t", ch, hex(ord(ch)), unicodedata.name(ch))

                # breathing must be correct (if not number or latin or uppercase)

                if (
                    not re.match(NUMBER, word) and
                    not re.match(LATIN, word) and
                    not word == word.upper()
                ):
                    d = unicodedata.normalize("NFD", word.lower())
                    if d[0] in "αεηιοω":
                        if d[1] in "\u0313\u0314":
                            pass
                        elif d[1] in "ιυ":
                            if d[2] in "\u0313\u0314":
                                pass
                            else:
                                error(fname, lnum, word, "BREATHING ERROR")
                        else:
                            error(fname, lnum, word, "BREATHING ERROR")
