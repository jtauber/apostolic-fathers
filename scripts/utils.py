from unicodedata import normalize, category

def real_len(s):
    l = 0
    for ch in normalize("NFD", s):
        if category(ch)[0] != "M":
            l += 1
    return l


def real_just(t, l):
    return t + (" " * (l - real_len(t)))


def print_interlinear(token_lists, fout):
    max_len = [max(map(real_len, x)) for x in zip(*token_lists)]
    print(file=fout)
    for token_list in token_lists:
        print(
            " ".join(
                real_just(t, l) for l, t in zip(max_len, token_list)
            ).strip(),
            file=fout
        )
