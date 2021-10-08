matrix = []
while True:
    inp = input()
    if inp.lower() == "end":
        break
    row = [int(i) for i in inp.split()]

    matrix.append(row)

m = len(matrix)  # rows
n = len(matrix[0])  # columns

outMatrix = [
    [0 for j in range(n)] for i in range(m)
]

for i in range(m):
    for j in range(n):
        outMatrix[i][j] += matrix[i-1][j]
        outMatrix[i][j] += matrix[i][j-1]
        if i+1 == m:
            outMatrix[i][j] += matrix[0][j]
        else:
            outMatrix[i][j] += matrix[i+1][j]

        if j+1 == n:
            outMatrix[i][j] += matrix[i][0]
        else:
            outMatrix[i][j] += matrix[i][j+1]

        print(outMatrix[i][j], end=' ')
    print()
