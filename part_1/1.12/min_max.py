a, b, c = int(input()), int(input()), int(input())

min_number, max_number = 0, 0

if a >= b and a >= c:
    max_number = a
if b >= a and b >= c:
    max_number = b
if c >= a and c >= b:
    max_number = c

print(max_number)

if a <= b and a <= c:
    min_number = a
if b <= a and b <= c:
    min_number = b
if c <= a and c <= b:
    min_number = c

print(min_number)

meh = a + b + c - max_number - min_number

print(meh)
