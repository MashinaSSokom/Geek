class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.length = len(matrix)
        self.width = len(matrix[0])

    def matrix_printer(self):
        for idx in range(self.length):
            if len(self.matrix[idx]) == self.width:
                line = f"| {' '.join(str(el) for el in self.matrix[idx])} |"
                print(line)
            else:
                raise ValueError("Разная длина строк матрицы")
        return 1


matrix_in_line = [[1, 2], [3, 4], [5, 6]]
mat = Matrix(matrix_in_line)
print(mat.matrix_printer())

