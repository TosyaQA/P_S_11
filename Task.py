#Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def print(self):
        matrixString = ""
        for i in range(len(self.matrix)):
            matrixString = matrixString + '  '.join(map(str,self.matrix[i])) + "\n"
        return matrixString
    
    def comparison(self, other):
        if self.matrix > other.matrix:
            return "Первая матрица больше второй"
        elif self.matrix < other.matrix:
            return "Вторая матрица больше первой"
        else:
            return "Матрицы равны"
    
    def add(self, other):
        result = []
        numbers = []

        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(summa)
                
                if len(numbers) == len(self.matrix[i]):
                    result.append(numbers)
                    numbers = []

        return result
    
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix1.print())
matrix2 = Matrix([[7, 8, 9], [1, 2, 3]])
print(matrix2.print())
print(matrix1.add(matrix2))
print(matrix1.comparison(matrix2))