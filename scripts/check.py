#!/usr/bin/env python3

import glob
import re
import unicodedata


ELLIPSIS = r"\.\.\."
LATIN = r"[A-Z]?[a-zë]+[\u002C\u002E\u003B\u003F]?"
NUMBER = r"[ιη]+[\u02B9]"


for filename in glob.glob("structured/*_CORRECTED.txt"):

    with open(filename) as f:

        prev_ref = None

        for line_num, line in enumerate(f, 1):
            parts = line.strip().split()

            # there can be no blank lines

            if not parts:
                print(f"{filename}: {line_num}: BLANK LINE")

            # tokens must be split by a single space

            if line != " ".join(parts) + "\n":
                print(f"{filename}: {line_num}: BAD WHITESPACE")

            # the first token must be a reference of the form <num>.<num>

            if not re.match(r"\d+\.\d+$", parts[0]):
                print(f"{filename}: {line_num}: BAD REFERENCE FORM")

            # references must be in sort order

            ref = tuple(int(i) for i in parts[0].split("."))

            if prev_ref and ref <= prev_ref:
                print(f"{filename}: {line_num}: BAD REFERENCE ORDERING")

            prev_ref = ref

            for word in parts[1:]:

                # word must be NFKC normalized

                if word != unicodedata.normalize("NFKC", word):
                    print(f"{filename}: {line_num}: BAD UNICODE NORMALIZATION")

                # word must contain value sequence of Greek characters

                if not re.match(fr"({ELLIPSIS}|{LATIN}|{NUMBER}|\(?[\u0374\u0390-\u03A1\u03A3-\u03C1\u03C3-\u03CE\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC]+\u03C2?\)?[\u02BC]?[\u002C\u002E\u003B\u00B7]?\)?\*?)$", word):
                    print(f"{filename}: {line_num}: {word}: BAD WORD")
                    for ch in word:
                        print(ch, hex(ord(ch)), unicodedata.name(ch))

                # breathing must be correct (if not number or latin)

                if not re.match(NUMBER, word) and not re.match(LATIN, word):
                    d = unicodedata.normalize("NFD", word.lower())
                    if d[0] in "αεηιοω":
                        if d[1] in "\u0313\u0314":
                            pass
                        elif d[1] in "ιυ":
                            if d[2] in "\u0313\u0314":
                                pass
                            else:
                                print(f"{filename}: {line_num}: {word}: BREATHING ERROR")
                        else:
                            print(f"{filename}: {line_num}: {word}: BREATHING ERROR")
