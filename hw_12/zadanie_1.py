import random
lst = [random.randint(1, 10) for i in range(10)]
val = random.randint(5, 10)
print('Список : ', lst)
print('Значение для сравнения : ', val)


def func(x, y):
    k = False
    for i in x:
        for j in x:
            sums = i + j
            if sums == y:
                k = True
    return k


print(func(lst, val))
