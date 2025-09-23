def transpose(matrix):

    n = len(matrix)

    transposed = []

    for j in range(n):
        new_row = []
        for i in range(n):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


print(transpose([[3, 0, 11], [1, 2, 9], [7, 4, 3]]))