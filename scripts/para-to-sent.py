#!/usr/bin/env python3

"""
converts the textpart-per-paragraph to textpart-per-sentence.
"""


for input_filename, output_filename in [
    ("text/012-barnabas.txt", "text/012-barnabas.sent.txt"),
]:
    with open(input_filename) as f, open(output_filename, "w") as g:
        for line in f:
            line = line.strip()
            ref, text = line.split(maxsplit=1)
            # if ref.endswith(".0"):  # ignore headings
            #     continue
            sentence = []
            sent_num = 1
            for token in text.split():
                sentence.append(token)
                if "." in token or ";" in token or "·" in token:
                    print(f"{ref}.{sent_num} {' '.join(sentence)}", file=g)
                    sent_num += 1
                    sentence = []
        assert sentence == [], "finished para mid-sentence"
