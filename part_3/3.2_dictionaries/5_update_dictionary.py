def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key * 2 in d:
        d[key * 2] += [value]
    else:
        d[key * 2] = [value]
