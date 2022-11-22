func = lambda x, y=2: x**y
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [5, 6, 7, 8, 9]
g = list(map(func, lst_1))
h = list(map(func, lst_1, lst_2))
print('Применение map для одного списка : ', g)
print('Применение map для двух списков : ', h)
