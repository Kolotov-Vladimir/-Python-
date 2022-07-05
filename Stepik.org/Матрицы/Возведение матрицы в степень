#Напишите программу, которая возводит квадратную матрицу в m-ую степень.

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.

#Формат выходных данных
#Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

#Тестовые данные 
#Sample Input 1:

#3
#1 2 3
#4 5 6
#7 8 9
#2
#Sample Output 1:

#30 36 42
#66 81 96
#102 126 150
#Sample Input 2:

#3
#1 2 1
#3 3 3
#1 2 1
#5
#Sample Output 2:

#1666 2222 1666
#3333 4443 3333
#1666 2222 1666
#Sample Input 3:

#5
#1 2 1 1 2
#3 3 3 3 3
#1 2 1 1 2
#3 3 3 3 3
#1 2 1 1 2
#3
#Sample Output 3:

#133 176 133 133 176
#279 369 279 279 369
#133 176 133 133 176
#279 369 279 279 369
#133 176 133 133 176

#Решение
n = int(input()) # размер квадратной матрицы
def input_matrix(): #функция заполнения матрицы
    matrix = []
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix
def power(matrix, n, p):  #функция возведение матрицы в степень
    result = matrix[:]
    while p:
        t_result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    t_result [i][j] += matrix[i][k] * result[k][j]
        result = t_result [:]
        p -= 1   
    return result
matrix1 = input_matrix()
p = int(input()) #степень матрицы
mx = power(matrix1, n, p-1)
for k in range(len(mx)):
    print(*mx[k])
