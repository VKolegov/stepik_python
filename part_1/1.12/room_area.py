room_type = input()

if room_type == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2  # полупериметр

    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print(S)

elif room_type == "прямоугольник":
    a = float(input())
    b = float(input())

    S = a * b

    print(S)

elif room_type == "круг":
    r = float(input())

    S = 3.14 * r ** 2

    print(S)
