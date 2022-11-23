#Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, ... , n^2
#так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
#Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по nn чисел в каждой, разделённые пробелами.

#Формат выходных данных
#Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

#Тестовые данные
#Sample Input 1:

#3
#8 1 6
#3 5 7
#4 9 2
#Sample Output 1:

#YES
#Sample Input 2:

#3
#8 2 6
#3 5 7
#4 9 1
#Sample Output 2:

#NO
#Sample Input 3:

#3
#4 9 2
#3 5 7
#8 1 6
#Sample Output 3:

#YES

#Решение
n = int(input())
matrix = []
def input_matrix(): #функция заполнения матрицы
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix
matrix = input_matrix()
gl = 0
pb = 0
st = 0
t = True
l = [num for num in range(1, n **2 +1)]
for i in range(n):
    count = [x[0] for x in matrix]
    count = sum(count)
for i in range(n):
    x = [x[i] for x in matrix]
    if sum(x) != count:
        t = False
    for j in range(n):
        if matrix[i][j] in l:
            l.remove(matrix[i][j])
        else:
            t = False
        if matrix[i][j] == 0:
            t = False
        gl += matrix[i][i]
        pb += matrix[i][n - i - 1]
    for k in range(len(x)):
        st += x[k]

if gl == pb == st and t == True:
    print('YES')
else:
    print('NO')
