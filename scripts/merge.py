#!/usr/bin/env python3

from itertools import zip_longest
from unicodedata import normalize

WORK = "003-ignatius-ephesians"

A = {}
B = {}
C = {}

D = set()

with open(f"structured/{WORK}_CCEL.txt") as f:
    for line in f:
        line = normalize("NFC", line).replace("\u2019", "\u02BC")
        ref = line.strip().split()[0]
        text = line.strip().split()[1:]
        A[ref] = text
        D.add(tuple(int(p) for p in ref.split(".")))

with open(f"structured/{WORK}_OGL.txt") as f:
    for line in f:
        line = normalize("NFC", line).replace("\u2019", "\u02BC")
        line = line.replace(":", "·")
        line = line.replace(" ἀλλ̓ ", " ἀλλʼ ")
        line = line.replace(" κατ̓ ", " κατʼ ")
        line = line.replace(" καθ̓ ", " καθʼ ")
        line = line.replace(" μετ̓ ", " μετʼ ")
        line = line.replace(" παῤ ", "παρʼ")
        line = line.replace(" ἀπ̓ ", " ἀπʼ ")
        line = line.replace(" ἀφ̓ ", " ἀφʼ ")
        line = line.replace(" δἰ ", " διʼ ")
        line = line.replace(" ἐπ̓ ", " ἐπʼ ")
        line = line.replace(" ἐφ̓ ", " ἐφʼ ")
        line = line.replace(" ὑπ̓ ", " ὑπʼ ")
        line = line.replace(" ὑφ̓ ", " ὑφʼ ")
        ref = line.strip().split()[0]
        text = line.strip().split()[1:]
        B[ref] = text
        D.add(tuple(int(p) for p in ref.split(".")))

with open(f"structured/{WORK}_LOGOS.txt") as f:
    for line in f:
        line = normalize("NFC", line).replace("\u2019", "\u02BC")
        ref = line.strip().split()[0]
        text = line.strip().split()[1:]
        C[ref] = text
        D.add(tuple(int(p) for p in ref.split(".")))

for r, s in sorted(D):
    ref = f"{r}.{s}"
    print()
    print(ref)
    print()
    for a, b, c in zip_longest(A.get(ref, []), B.get(ref, []), C.get(ref, [])):
        if a != b and b == c:
            X = "bc"
        elif a == b and b != c:
            X = "ab"
        elif a == c and a != b:
            X = "ac"
        elif a != b and b != c:
            X = "@@"
        else:
            X = " "
        a = a or "-"
        b = b or "-"
        c = c or "-"
        print(f"  {X:5s} {a:20s}\t{b:20s}\t{c:20s}")
