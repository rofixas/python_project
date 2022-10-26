print('Введите год')

god = int(input())
if (1900 < god < 1000000 and god % 4 == 0 and god % 100 != 0 or god % 400 == 0):

    print('Год высокосный')
elif 1900 < god < 1000000:

    print('Год не высокосный')
else:

    print('Год не соответствует условиям ')