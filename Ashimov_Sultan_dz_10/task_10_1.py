class Matrix:
    def __init__(self, matrix:list):
        self.matrix = matrix
        self.length = len(matrix)
        self.width = len(matrix[0])

    def get_matrix(self):
        return self.matrix

    def __str__(self):
        end = []
        for idx in range(self.length):
            if len(self.matrix[idx]) == self.width:
                line = f"| {' '.join(str(el) for el in self.matrix[idx])} |"
                end.append(line)
            else:
                raise ValueError("Разная длина строк матрицы")
        return "\n".join(el for el in end)

    def __add__(self, other: list):
        matrix2 = other.get_matrix()
        matrix_sum = []
        end = []
        if self.length == len(matrix2):
            for i in range(self.length):
                line = []
                if self.width == len(self.matrix[i]) == len(matrix2[i]):
                    for j in range(self.width):
                        line.append(self.matrix[i][j] + matrix2[i][j])
                    matrix_sum.append(line)
                else:
                    raise ValueError(f"Разная длина строк №{i+1}")
            for idx in range(self.length):
                if len(matrix_sum[idx]) == self.width:
                    line = f"| {' '.join(str(el) for el in matrix_sum[idx])} |"
                    end.append(line)
                else:
                    raise ValueError("Разная длина строк матрицы")
            return "\n".join(el for el in end)
        raise ValueError("Разная кол-во строк в матрицах")


matrix_in_line = [[1, 2], [3, 4], [5, 6]]
matrix_in_line2 = [[1, 3], [3, 4], [5, 6]]

mat1 = Matrix(matrix_in_line)
print("\nМатрица #1 \n")
print(mat1)
mat2 = Matrix(matrix_in_line2)
print("\nМатрица #2 \n")
print(mat2)
print("\nСумма мартиц \n")
print(mat1+mat2)
