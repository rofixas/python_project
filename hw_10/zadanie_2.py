import random
m = 1
dict_1 = {'a' : [random.randint(1, 20) for i in range(1, 21)]}
print(dict_1)
for i in dict_1.values():
    for j in i:
        m = m * j
print('Произведение всех элементов по ключу "а" :', m)