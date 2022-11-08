a = input('Введите предложение с более чем 2 словами : ')
b = sorted(a.split(" "))
b = list(filter(None, b))

for i in b:
    print(f'{b.index(i):<8}', i)
print("Количество слов : ", len(b))
