h = int(input())
while 3 <= h <= 9:
    for i in range(1,h):
        for j in range(1,i):
            print(j, end=' ')

        print(i)
    break