#Напишите программу, которая меняет местами столбцы в матрице.

#Формат входных данных
#На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

#Формат выходных данных
#Программа должна вывести указанную таблицу с замененными столбцами.

#Тестовые данные
#Sample Input 1:

#3
#4
#11 12 13 14
#21 22 23 24
#31 32 33 34
#0 1
#Sample Output 1:

#12 11 13 14
#22 21 23 24
#32 31 33 34
#Sample Input 2:

#3
#3
#11 12 13
#21 22 23
#31 32 33
#2 1
#Sample Output 2:

#11 13 12 
#21 23 22 
#31 33 32 
#Sample Input 3:

#3
#5
#12 14 11 13 24
#22 24 21 23 14
#32 34 31 33 34
#0 2
#Sample Output 3:

#11 14 12 13 24
#21 24 22 23 14
#31 34 32 33 34

#Решнение
n, m = int(input()), int(input())
matrix = []
def input_matrix(): #функция заполнения матрицы
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix
matrix = input_matrix()
ij = [int(num) for num in input().split()]
for i in range(n):
    for j in range(m):
        if j == int(ij[0]):
            matrix[i][j], matrix[i][int(ij[1])] = matrix[i][int(ij[1])], matrix[i][j]
for k in range(n):
    print(*matrix[k])
