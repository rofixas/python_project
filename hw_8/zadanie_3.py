a = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
b = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
c = []

for i in a:
    if i in b : # and i not in c , в случае если одинаковые элементы удалять из списка "b" , 2 в таком случае будет встречаться 1 раз
        c.append(i)

print(c)
for j in c:
    g = c.count(j)
    print('Элемент списка :' , j , 'Встречается ' , g , ' раз')

