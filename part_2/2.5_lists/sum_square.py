s = 0

nums = []

while True:
    x = int(input())
    s += x
    nums += [x]

    if s == 0:
        break

sq = 0
for i in nums:
    sq += i * i
print(sq)
