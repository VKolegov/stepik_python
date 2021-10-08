n = int(input())

# n x n zero matrix
mat = [
    [0 for j in range(n)] for i in range(n)
]

s = range(1, n * n + 1)  # 1 ... 25

t = -1  # top boundary
b = n  # bottom boundary
l = -1  # left boundary
r = n  # right boundary
row = 0
col = 0

rM = 0  # row modification
cM = 1  # column modification

i = 0
while i < n * n:
    #  direction right
    if cM == 1 and col == r:
        # print("moving down")

        #  двигаемся вниз
        cM = 0
        rM = 1

        #  возвращаемся в границы
        col -= 1
        row += 1

        # меняем верхнюю границу
        t += 1
        continue

    #  direction down
    if rM == 1 and row == b:
        # print("moving left")

        #  двигаемся влево
        cM = -1
        rM = 0

        #  возвращаемся в границы
        row -= 1
        col -= 1

        # меняем правую границу
        r -= 1
        continue

    # direction left
    if cM == -1 and col == l:
        # print("moving up")

        #  двигаемся вверх
        cM = 0
        rM = -1

        #  возвращаемся в границы
        row -= 1
        col += 1

        # меняем нижнюю границу
        b -= 1
        continue

    if rM == -1 and row == t:
        # print("moving right")

        #  двигаемся вправо
        cM = 1
        rM = 0

        #  возвращаемся в границы
        row += 1
        col += 1

        # меняем левую границу
        l += 1
        continue

    mat[row][col] = s[i]

    row += rM
    col += cM
    i += 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
