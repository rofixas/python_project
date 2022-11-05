n = int(input('Введите высоту пирамиды : '))
num = '1000000000000000'
for i in range(n):
    b = num[i::-1]
    print(f'{i:<5}' , ' ' * (n) , b[i::-1])
    n -= 1
