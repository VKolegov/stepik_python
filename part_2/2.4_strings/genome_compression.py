dna = input()

compressed = ""
i = 0
l = len(dna)

while i < l:
    char = dna[i]
    compressed += char
    c = 0
    for j in range(i, l):
        if dna[j] == char:
            c += 1
        else:
            break
        i += 1

    compressed += str(c)

print(compressed)
