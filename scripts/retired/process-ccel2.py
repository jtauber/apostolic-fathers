#!/usr/bin/env python3

import re
import roman

with open("raw-ccel-lake/013-shepherd.txt") as f:
    bk = 0
    ch = 0
    vs = 0
    for line in f:
        if line.startswith("@ "):
            bk += 1
            assert int(line.split()[1]) == bk
            ch = 0
            vs = 0
            print()
            print(f"{bk}.{ch}.{vs}", " ".join(line.split()[2:]), end="")
            ch = 1
        elif re.match(r"^[IVXL]+\n$", line):
            ch = roman.fromRoman(line.strip())
            vs = 0
        elif re.match(r"^(\d+)\. ", line):
            for token in line.split():
                if re.match(r"^(\d+)\.$", token):
                    vs = int(token[:-1])
                    print()
                    print(f"{bk}.{ch}.{vs}", end=" ")
                else:
                    print(token, end=" ")
        else:
            print()
            print(f"{bk}.{ch}.{vs}", end=" ")
            for token in line.split():
                print(token, end=" ")
            print()
