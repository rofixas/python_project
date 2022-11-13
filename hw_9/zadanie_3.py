import random
sumchet = 0
sumnechet = 0
l = [random.randint(1, 15) for i in range(1, 16)]
print(l)
for i in range(len(l)):
    if l[i] % 2 == 0:
        sumchet += l[i]
    if l[i] % 2 != 0:
        sumnechet += l[i]
print('Сумма четных чисел списка : ', sumchet)
print('Сумма не четных чисел списка : ', sumnechet)
if sumchet > sumnechet:
    print("Сумма четных чисел списка больше")
elif sumchet == sumnechet:
    print('Везунчик , сумма четных чисел равна сумме не четных')
else:
    print('Сумма нечетных чисел списка больше')