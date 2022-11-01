print('Введите 2 слова')
a = ' '
while True:
    if a.count(' ') >= 2 or a.count(' ') == 0:
     print('Введите 2 слова')
    a = input()
    if a.count(' ') == 1:
        b = a[::-1]
        c = b.title()
        print(c)
        break
