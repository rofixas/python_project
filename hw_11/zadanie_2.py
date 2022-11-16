import random
list_1 = set([random.randint(1, 10) for i in range(1, 10)])
list_2 = set([random.randint(1, 20) for j in range(1, 10)])
print(set(list_1 | list_2))
print('Количество разных цифр : ', len(set(list_1 | list_2)))