matrix = [
    [1, 2],
    [4, 5],
    [7, 8]
]
n=len(matrix[0])
m=len(matrix)
def create_matrix(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    return matrix

matrix1 = create_matrix(n, m)

for row in matrix:
    print(row)
print('------------------------')
for i in range(m):
    for j in range(n):
        matrix1[j][i] = matrix[i][j]

for row in matrix1:
    print(row)
