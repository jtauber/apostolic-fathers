#!/usr/bin/env python3

import re
import roman

# for all files but Hermas

# note that the output is still slightly tweaked by hand, this just does
# most of the heavy lifting

with open("logos/014-martyrdom.txt") as f:
    ch = 0
    vs = 0
    for line in f:
        if re.match(r"^[IVXL]+\n$", line):
            ch = roman.fromRoman(line.strip())
            vs = 0
        elif re.match(r"^ ?(\d+) ", line):
            for token in line.split():
                if re.match(r"^(\d+)$", token.strip()):
                    vs = int(token.strip())
                    print()
                    print(f"{ch}.{vs}", end=" ")
                else:
                    print(token, end=" ")
        else:
            print()
            print(f"{ch}.{vs}", end=" ")
            for token in line.split():
                print(token, end=" ")
            print()
