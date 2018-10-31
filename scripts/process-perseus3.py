#!/usr/bin/env python3

import re

from lxml import etree

NS = {"TEI": "http://www.tei-c.org/ns/1.0"}

with open("raw-ogl-lake/tlg1419.tlg001.1st1K-grc1.xml") as f:
    tree = etree.parse(f)
    for part in tree.xpath("TEI:text/TEI:body/TEI:div[@type='edition']/TEI:div[@type='textpart']", namespaces=NS):
        assert part.attrib["subtype"] == "book"
        book = int(part.attrib["n"])
        for child in part:
            if child.tag == "{http://www.tei-c.org/ns/1.0}head":
                chapter = 0
                verse = 0
                text = re.sub("\s+", " ", child.xpath("string()").strip())
                print(f"{book}.{chapter}.{verse} {text}")
            elif child.tag == "{http://www.tei-c.org/ns/1.0}div":
                assert child.attrib["subtype"] == "chapter"
                chapter = int(child.attrib["n"])
                for gchild in child:
                    if gchild.tag == "{http://www.tei-c.org/ns/1.0}div":
                        assert gchild.attrib["subtype"] == "section"
                        verse = int(gchild.attrib["n"])
                        print(f"{book}.{chapter}.{verse}", end="")
                        for ggchild in gchild:
                            if ggchild.tag == "{http://www.tei-c.org/ns/1.0}p":
                                print("", re.sub("\s+", " ", ggchild.text).strip(), end="")
                                for gggchild in ggchild:
                                    print("", re.sub("\s+", " ", gggchild.tail).strip(), end="")
                            else:
                                assert False
                        print()
                    else:
                        assert False
            else:
                assert False
