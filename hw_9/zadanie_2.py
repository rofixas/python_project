import random
diag = 0
n = int(input('Введите размер матрицы : '))
m = [
    [random.randint(0, 10) for i in range(n)] for j in range(n)
]
for i in m:
    print(i)
for i in range(n):
     for j in range(n):
         if i == j:
             diag += m[i][j]
print('Сумма диагонали : ', diag)
for i in range(n):
    s = 0
    for j in range(n):
        s += m[j][i]
    print('Сумма ', i, 'Столбца : ', s)

# У меня не получилось сделать все компактно , поэтому я создал миллион циклов.