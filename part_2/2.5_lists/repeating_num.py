n = int(input())

c = 0
for i in range(1, n+1):
    for j in range(i):
        if c < n:
            print(i, end=' ')
            c += 1
