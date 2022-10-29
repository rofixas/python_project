a = int(input())
sum = 0
kol = 0
max = 0
min = 0
chet = 0
nechet = 0
while True:
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
    if a == 0:
        break
print('Сумма всех чисел', sum)
print('Среднее значение' ,(sum / kol))
print('Максимальное значение' , max)
print('Минимальное значение', min)
print(chet)
print(nechet)
# У меня не получилось вывести корректно минимальное значение ( ноль учитывается ) , а так же четные и нечетные числа