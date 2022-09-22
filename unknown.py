def unknown(count, n):
    count = count.copy()
    count["<unk>"] = 0
    del_keys = set()
    for n_gram in count:
        if n >= count[n_gram] > 0:
            count["<unk>"] += 1
            del_keys.add(n_gram)

    for key in del_keys:
        del count[key]

    return count, del_keys


def unknown_tokens_process(tokens, del_keys):
    new_tokens = tokens
    for i in range(len(new_tokens)):
        token = new_tokens[i]
        if token in del_keys:
            new_tokens[i] = "<unk>"

    return new_tokens
