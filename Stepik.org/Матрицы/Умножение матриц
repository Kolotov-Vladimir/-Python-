#Напишите программу, которая перемножает две матрицы.

#Формат входных данных
#На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. 
#Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.

#Формат выходных данных
#Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

#Тестовые данные 
#Sample Input 1:

#2 2
#1 2
#3 2

#2 2
#3 2
#1 1
#Sample Output 1:

#5 4
#11 8
#Sample Input 2:

#3 2
#2 5
#6 7
#1 8

#2 3
#1 2 1
#0 1 0
#Sample Output 2:

#2 9 2
#6 19 6
#1 10 1
#Sample Input 3:

#3 3
#2 4 6
#1 3 5
#0 4 8

#3 3
#6 3 1
#9 6 3
#0 2 0
#Sample Output 3:

#48 42 14
#33 31 10
#36 40 12


#Решение


def input_matrix(): #функция заполнения матрицы
    n = [int(num) for num in input().split()]
    matrix = []
    for i in range(n[0]):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix
def mx_mult(matrix1, matrix2):#Функция умножения матриц
    n = len(matrix1)
    k = len(matrix2[0])
    op = len(matrix1[0])
    mx3 = [[0] * k for i in range(n)]
    if len(matrix1[0]) != len(matrix2):
        print("Error: matrices are dimensionally inconsistent!")
        return mx3
    for i in range(n):
        for j in range(k):
            for x in range(op):
                mx3[i][j] += matrix1[i][x] * matrix2[x][j]
    return mx3
matrix1 = input_matrix()
input()
matrix2 = input_matrix()
mx = mx_mult(matrix1,matrix2)
for k in range(len(mx)):
    print(*mx[k])
