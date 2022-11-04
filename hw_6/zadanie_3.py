num = input('Введите символы для пирамиды : ')
n = int(input('Введите высоту пирамиды : '))

for i in range(n):
    b = num[i::-1]
    print(b[::-1])