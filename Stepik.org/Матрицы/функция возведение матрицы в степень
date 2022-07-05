#n - размер матрицы
#p - степерь
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
