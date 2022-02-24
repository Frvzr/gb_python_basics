from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix) - 1):
            if len(self.matrix[i]) != len(self.matrix[i + 1]):
                raise ValueError('fail initialization matrix')
        
    def __str__(self):
        matrix_txt = ""
        for i in range(len(self.matrix)):
            temp = ""
            for j in range(len(self.matrix[i])): 
                temp += f' {self.matrix[i][j]}'
            matrix_txt +=f'|{temp} |\n'
        return matrix_txt
    
    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3,], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    print(first_matrix + second_matrix)