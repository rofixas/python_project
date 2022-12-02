def dec(func):

    def wrapper(*args):
        for i in func(*args):
            if i % 3 == 0:
                k = 'Кратное 3'
            if i % 3 > 0:
                k = 'Не кратное 3'
            if i % 2 == 0:
                l = 'Парное'
            if i % 2 > 0:
                l = 'Не парное'
            print(f"{i:<3}", f"{k:<15}", l)
    return wrapper


@dec
def func_s(s):
    m = set(
        [i for i in range(1, s+1)]
    )
    print(m)
    return m


s = int(input())
func_s(s)
