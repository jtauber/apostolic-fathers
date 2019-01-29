#!/usr/bin/env python3

import fileinput

with fileinput.input() as f:
    for line in f:
        print(line.strip().replace("\u02BC", "\u2019"))
