a_orig = int(input())
b_orig = int(input())

# bruteforce
# if a >= b:
#     d = a
# else:
#     d = b

# while d % a != 0 or d % b != 0:
#     d += 1

# euclidean
a = a_orig
b = b_orig

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

gcd = a + b  # НОД - одна из переменных, вторая - ноль

lcm = (a_orig * b_orig) // gcd

print(lcm)
