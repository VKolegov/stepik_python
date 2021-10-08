a = int(input())
b = int(input())

count = 0
s = 0
mean = 0

for i in range(a, b+1):
    if i % 3 == 0:
        count += 1
        s += i

mean = s / count

print(mean)
