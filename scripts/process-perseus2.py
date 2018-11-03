#!/usr/bin/env python3

import re

from lxml import etree

NS = {"TEI": "http://www.tei-c.org/ns/1.0"}

# just for Barnabas which follows a slightly different structure

with open("raw-ogl-lake/tlg1216.tlg001.perseus-grc1.xml") as f:
    tree = etree.parse(f)
    for part in tree.xpath("text/body/div1"):
        assert part.attrib["type"] == "chapter"
        chapter = int(part.attrib["n"])
        for child in part:
            if child.tag == "p":
                verse = 0
                text = re.sub(r"\s+", " ", child.xpath("string()").strip())
                print(f"{chapter}.{verse} {text}")
            elif child.tag == "div2":
                assert child.attrib["type"] == "section"
                verse = int(child.attrib["n"])
                print(f"{chapter}.{verse}", end="")
                for gchild in child:
                    if gchild.tag == "p":
                        print("", re.sub(r"\s+", " ", gchild.text).strip(), end="")
                        for ggchild in gchild:
                            print("", re.sub(r"\s+", " ", ggchild.tail).strip(), end="")
                    else:
                        assert False
                print()
            else:
                assert False
