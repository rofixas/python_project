def dec(func):
    def wrapper(*args):
        while True:
            pas = func(*args)
            if pas is None:
                print('Пароль не должен содержать пробелов и пустых строк, попробуйте еще раз')
            elif len(pas) < 8:
                print('Ваш пароль меньше 8 символов, попробуйте еще раз')
            elif len([i for i in pas if i.isalpha()]) == 0:
                print('Ваш пароль должен содержать хотя бы 1 букву, попробуйте еще раз')
            elif len([i for i in pas if i.isdigit()]) == 0:
                print('Ваш пароль должен содержать хотя бы 1 цифру, попробуйте еще раз')
            elif len([i for i in pas if i.isalnum()]) == len(pas):
                print('Ваш пароль должен соддержать хотя бы 1 спец символ, попробуйте еще раз')
            else:
                print('Пароль соответстует условиям')
                print('Вашь пароль : ', pas)

                break
    return wrapper


@dec
def pasw():
    print('*'*10)
    print(
        'Введите пароль который содержит хотя бы 1 цифру , 1 букву , и 1 спец. символ и состоит из 8 и более символов..'
    )
    lst = input()
    cnt = lst.count(' ')
    if cnt > 0 or len(str(lst)) == 0 or '\t' in lst:
        lst = None  # Можно было бы использовать метод isspace, но я уже не стал исправлять

    return lst


pasw()
