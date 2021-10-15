n = int(input())

x = 0
y = 0
for _ in range(n):
    command = input().lower().split()

    dX = 0
    dY = 0

    direction = command[0]
    change = int(command[1])

    if direction == "север":
        dY = change
    elif direction == "восток":
        dX = change
    elif direction == "юг":
        dY = -change
    elif direction == "запад":
        dX = -change

    x += dX
    y += dY

print(x, y)
