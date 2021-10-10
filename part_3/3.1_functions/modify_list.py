def modify_list(l):
    lim = len(l)
    i = 0
    while i < lim:
        # even
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        # odd
        else:
            del l[i]
            i -= 1
            lim = len(l)

        i += 1
