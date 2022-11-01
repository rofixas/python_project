a = int(input('Введите натуральные числа '))
sum = 0
kol = 0
max = a
min = a
chet = 0
nechet = 0
while True:
    if a == 0:
        break
    sum += a
    kol += 1
    a = int(input())
    if a > max:
        max = a
    if a < min:
        min = a
    if a % 2 == 0:
        chet += 1
    if a % 2 != 0:
        nechet += 1
print('Сумма всех чисел', sum)
print('Среднее значение' ,(sum / kol))
print('Максимальное значение' , max)
print('Минимальное значение', min)
print(chet)
print(nechet)
# У меня не получилось вывести корректно минимальное значение ( ноль учитывается ) , а так же четные и нечетные числа