import random

def is_valid(string):
    return string.isdigit() and 0 < int(string) <= int(right)

def is_valid_r(string):
    return string.isdigit() and 2 < int(string)

def error():
    print(f'А может быть все-таки введем целое число от 1 до {int(right)}?')
    print('Введите число:')
    return input()

new_game = 'д'
print('Добро пожаловать в числовую угадайку')
while new_game == 'д':
    attempts = 1
    print('Укажите правую границу угадываемого числа:')
    right = input()
    while is_valid_r(right) == False:
        print('Введено неверное значение! Введите целое число больше 2:')
        right = input()
    num = random.randrange(1, int(right) + 1)
    print('Введите число:')
    m = input()
    while is_valid(m) == False:
        m = error()
    while int(m) != num:
        attempts += 1
        if int(m) < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            m = input()
            while is_valid(m) == False:
                m = error()
        if int(m) > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            m = input()
            while is_valid(m) == False:
                m = error()
        if int(m) == num:
            print('Вы угадали, поздравляем!')
            print('Вы угадали за', attempts, 'раз')
            print('Спасибо, что играли в числовую угадайку. Хотите сыграть ещё раз?')
            new_game = input('Введите: д / н\n')
            if new_game != 'д':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')