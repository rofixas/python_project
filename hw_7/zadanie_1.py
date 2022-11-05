sum = int(input('Введите сумму кредита на 1 год: '))
b = 12
p = 0.02
c = 60
k = 0.04
sum_1 = int(input('Введите сумму кредита на 5 лет: '))
print('Кредит на 1 год' + ' *'*100)
for i in range(1,b+1):
     plata = sum / b
     sum = sum - plata
     n = sum * p
     sum = sum + n
     print(i , 'месяц оплачивать : %.2f' % plata , '\tНачисленно процентов %.2f' % n)
print('Кредит на 5 лет' + ' *'*100)
for j in range(1,c+1):
     if j < 24:
          plata_1 = sum_1 / c
          sum_1 = sum_1 - plata_1
          m = sum_1 * p
          sum_1 = sum_1 + m
     else:
          plata_1 = sum_1 / c
          sum_1 = sum_1 - plata_1
          m = sum_1 * k
          sum_1 = sum_1 + m

     print(j, 'месяц оплачивать : %.2f' % plata_1, '\tНачисленно процентов %.2f' % m)

