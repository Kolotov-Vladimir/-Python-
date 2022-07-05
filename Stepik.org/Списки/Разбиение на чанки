#На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

#Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

#Формат входных данных
#На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

#Формат выходных данных
#Программа должна вывести указанный вложенный список.
#Sample Input 1:

#a b c d e f
#2
#Sample Output 1:

#[['a', 'b'], ['c', 'd'], ['e', 'f']]
#Sample Input 2:

#a b c d e f
#3
#Sample Output 2:

#[['a', 'b', 'c'], ['d', 'e', 'f']]
#Sample Input 3:

#a b c d e f
#6
#Sample Output 3:

#[['a', 'b', 'c', 'd', 'e', 'f']]
#Sample Input 4:

#a b c d e f r g b
#2
#Sample Output 4:

#[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
#Sample Input 5:

#a b
#3
#Sample Output 5:

#[['a', 'b']]

#Решение

l = [i for i in input().split() if i != ' ']
n = int(input())
new = [list(l[0])]
count = 1
if n >= len(l):
    print([l])
else:
    for i in range(1, len(l)):
        if i % n != 0:
            new[i-count].extend(list(l[i]))
            count += 1
            
        else:
            new.append(list(l[i]))
    print(new)
