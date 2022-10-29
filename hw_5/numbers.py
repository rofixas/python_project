print('Введите число')
a = int(input())
b = []      #Создание списка
while a:
    c = a % 10
    if c in b:
        print("Одинаковые числа есть")
        break
    else:
        b.append(c) # Команда добавляет число в конец списка
    a = a // 10
else:
    print("Одинаковых чисел нет")