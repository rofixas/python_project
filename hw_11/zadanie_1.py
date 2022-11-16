import random

list_1 = [random.randint(1, 11) for i in range(1, 15)]
print(list_1)
cnt = 0
for i in list_1:
    b = list_1.count(i)
    print(i, ' Встречается : ', b, ' раз')
    if b == 1:
        cnt += 1
print('*'*10)
if cnt == 1:
    print('В списке ', cnt, " Уникальное число")
elif cnt <= 4:
    print('В списке ', cnt, " Уникальных числа")
else:
    print('В списке ', cnt, " Уникальных чисел")



# # В случае если я не правильно понял задание , сделал еще следующим образом :
# list_1 = [random.randint(1, 11) for i in range(1, 15)]
# print(set(list_1))
# print('Количество элементов не учитвая одинаковые числа : ', len(set(list_1)))