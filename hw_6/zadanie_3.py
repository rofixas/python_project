# h = int(input())
# while 3 <= h <= 9:
#     for i in range(1,h):
#         for j in range(1,i):
#             print(j, end=' ')
#
#         print(i)
#     break
s = input()
l = len(s) // 2
while 3 <= l <= 9:
    for i in range(l, -1, -1):
        print(' ' * i, end=' ')
        print(s[i:-i - 1])
    break