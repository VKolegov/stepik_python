lst = [int(i) for i in input().split()]

x = int(input())

positions = []
for i in range(len(lst)):
    if lst[i] == x:
        positions += [i]

if len(positions) == 0:
    print("Отсутствует")
else:
    for i in sorted(positions):
        print(i, end=' ')
