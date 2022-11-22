import random
lst = []

def gen(n, z):

    for i in range(n, z+1):
        k = 0
        for j in range(1, i+1):
            if i % j == 0:
                k += 1
        if k == 2:
            lst.append(i)
    return lst


m = random.randint(1, 10)
c = random.randint(11, 100)
gen(m, c)
for i in lst:
    print(i, end=' ')

