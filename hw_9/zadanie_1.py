n = int(input('Введите размер матрицы : '))
m = [
    [j for i in range(n)] if j % 2 == 0 else [i for i in range(-n, 0)]
    for j in range(n)
]

for i in m:
    print(i)
