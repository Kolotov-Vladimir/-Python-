#Напишите программу, которая транспонирует квадратную матрицу.
#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.
#Формат выходных данных
#Программа должна вывести транспонированную матрицу.
#Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

#Тестовые данные 
#Sample Input 1:

#3
#1 2 3
#4 5 6
#7 8 9
#Sample Output 1:

#1 4 7
#2 5 8
#3 6 9
#Sample Input 2:

#4
#1 2 3 1
#4 5 6 4
#7 8 9 7
#1 2 3 8
#Sample Output 2:

#1 4 7 1
#2 5 8 2
#3 6 9 3
#1 4 7 8
#Sample Input 3:

#2
#5 6
#8 4
#Sample Output 3:

#5 8
#6 4

#Решение
n = int(input())
def input_matrix(): #функция заполнения матрицы
    matrix = []
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix
def print_matrix(matrix, n, width=1): #функция вывода матрицы
    for r in range(n):
        for c in range(n):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()
mx = input_matrix()
print_matrix(mx, n)
