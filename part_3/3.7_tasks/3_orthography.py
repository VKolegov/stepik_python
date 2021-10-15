n = int(input().strip())

dic = []
for i in range(n):
    dic += [input().strip().lower()]

l = int(input().strip())

lines = []
for i in range(l):
    lines += [input().strip().lower().split()]

errors = []
for line in lines:
    for word in line:
        if word not in dic and word not in errors:
            errors += [word]

print(*errors, sep='\n')
