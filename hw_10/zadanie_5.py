a = 'python is good laguage to code'
b = []
c = []
for i in a:
    if i != ' ':
        b.append(i)
print('Ключи словаря : ', b)
for j in range(len(b)):
    g = b.count(b[j])
    c.append(g)
print('Значения словаря : ', c)
print('Словарь : ', dict(zip(b, c)))
