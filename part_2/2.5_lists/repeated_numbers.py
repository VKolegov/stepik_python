a = [int(i) for i in input().split()]

seen = []
seen_twice = []

a.sort()

for x in a:
    if x not in seen:
        seen.append(x)
    elif x not in seen_twice:
        seen_twice.append(x)

for n in seen_twice:
    print(n, end=' ')
