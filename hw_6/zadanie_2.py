stroka = input('Введите строку в которой нужно искать символы: ')
char = input('Введите символ который нужно найти в строке: ')
cnt = 0
b = -1
while True:
    b = stroka.find(char, b+1)
    if b == -1:
        break
    cnt += 1
print('В предложении ' , cnt , 'количество заданных символов ')





