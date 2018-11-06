#!/usr/bin/env python3

from itertools import zip_longest
from unicodedata import normalize

WORK = "006-ignatius-romans"

LINES_1 = open(f"comparison/{WORK}_COMPARE_JT1.txt").readlines()
LINES_2 = open(f"comparison/{WORK}_COMPARE_SM1.txt").readlines()

assert len(LINES_1) == len(LINES_2)

line_num = 0
ref = None
for a, b in zip_longest(LINES_1, LINES_2):
    line_num += 1
    a = a.rstrip()
    b = b.rstrip()
    if a.startswith(" "):
        assert b.startswith(" ")
        a_parts = a.split("\t")
        b_parts = b.split("\t")
        assert len(a_parts) == len(b_parts), (line_num, a, b)
        assert a_parts[0] == b_parts[0], (line_num, a, b)
        assert a_parts[2] == b_parts[2], (line_num, a, b)
        a_tag = a_parts[0][:6].strip()
        b_tag = b_parts[0][:6].strip()
        assert a_tag == b_tag, (a_tag, b_tag)
        a_word = normalize("NFC", a_parts[1].strip())
        b_word = normalize("NFC", b_parts[1].strip())
        if a_word != b_word:
            print(f"{ref:5s} {line_num:6d} {a_tag:4s} {a_word:25s} {b_word:25s}")
    else:
        assert not b.startswith(" ")
        assert a == b
        if a:
            ref = a
