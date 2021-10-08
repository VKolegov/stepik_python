n = int(input())

s = ""

if n > 100:
    rem_2 = n % 100
else:
    rem_2 = n

if rem_2 < 20:
    rem = rem_2
else:
    rem = rem_2 % 10

if rem == 1:
    s = "программист"
elif 2 <= rem <= 4:
    s = "программиста"
else:
    s = "программистов"

print(n, s)
