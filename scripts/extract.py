#!/usr/bin/env python3

# once compare_JT_SM.py has not output, we can use this to generate the new
# corrected, structured text

from itertools import zip_longest
from unicodedata import normalize

WORK = "001-i_clement"

LINES_1 = open(f"comparison/{WORK}_COMPARE_JT2.txt").readlines()
LINES_2 = open(f"comparison/{WORK}_COMPARE_SM2.txt").readlines()

assert len(LINES_1) == len(LINES_2)

has_printed = False
line_num = 0
for a, b in zip(LINES_1, LINES_2):
    line_num += 1
    a = a.rstrip()
    b = b.rstrip()
    if a.startswith(" "):
        assert b.startswith(" ")
        a_parts = a.split("\t")
        b_parts = b.split("\t")
        assert len(a_parts) == len(b_parts)
        assert a_parts[0] == b_parts[0]
        assert a_parts[2] == b_parts[2]
        a_tag = a_parts[0][:6].strip()
        b_tag = b_parts[0][:6].strip()
        assert a_tag == b_tag
        a_word, b_word = normalize("NFC", a_parts[1].strip()), normalize("NFC", b_parts[1].strip())
        assert a_word == b_word
        if a_word != "-":
            print(a_word, end=" ")
    else:
        assert not b.startswith(" ")
        assert a == b
        if a:
            if has_printed:
                print()
            print(a, end=" ")
            has_printed = True
print()
