a = []
b = []
for i in range(10, 251):
    if i % 20 == 0:
        a.append(i)
    else:
        b.append(i)
print('Список чисел которые делятся на 20 без остатка : ', a)
print('Список чисел которые имеют остаток при делении на 20 : ', b)