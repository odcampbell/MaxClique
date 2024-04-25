def read_lower_triangular_matrix(file_path):# 0(N^2 + N)?
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 0(N)?

    # Split each line and convert to integers
    matrix = [list(map(int, line.split())) for line in lines]

    # Ensure the matrix is symmetric (copy lower triangular values to upper triangular)
    for i in range(len(matrix)): # 0(N)?
        for j in range(i + 1, len(matrix[i])): # 0(N)?
            matrix[j][i] = matrix[i][j]

    return matrix
# end read lower triangle


def create_full_matrix(lower_triangle_matrix): # O(N)
    size = len(lower_triangle_matrix)

    # Create a full matrix and fill it using the lower triangular matrix
    full_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i + 1):
            full_matrix[i][j] = lower_triangle_matrix[i][j]
            full_matrix[j][i] = lower_triangle_matrix[i][j]

    return full_matrix
# end full matrix