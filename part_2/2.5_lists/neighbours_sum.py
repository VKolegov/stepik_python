a = [int(i) for i in input().split()]

if len(a) == 1:
    print(a[0])
    exit()

for i in range(len(a)):
    s = a[i-1]
    if i + 1 == len(a):
        s += a[0]
    else:
        s += a[i+1]
    print(s, end=' ')
