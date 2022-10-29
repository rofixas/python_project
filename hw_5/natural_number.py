n = int(input())
for i in range(1, n):
    a = str(i)
    b = str(i**2)
    if a in b[-len(a):]: # Функция len для того что бы сравнить последние числа полученного числа , а не все число целиком.
        print(i , b)

