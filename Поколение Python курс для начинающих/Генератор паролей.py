import random

def is_digit_valid(string):
    return string.isdigit() and 0 < int(string) < 1001

def is_string_valid(string):
    return string == 'д' or string == 'н'

def generate_password(length, char):
        password = ''
        for _ in range(length):
            password += random.choice(char)
        return password

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
SYMBOLS = 'il1Lo0O'
chars = ''

passwords_quantity = input('Введите количество паролей для генерации:')
while is_digit_valid(passwords_quantity) == False:
    print('Ошибка ввода! Введите цифры от 1 до 1000:')
    passwords_quantity = input()
passwords_quantity = int(passwords_quantity)

password_length = input('Введите длину одного пароля:')
while is_digit_valid(password_length) == False:
    print('Ошибка ввода! Введите цифры от 1 до 1000:')
    password_length = input()
password_length = int(password_length)

while chars == '':
    is_include_digits = input('Включать ли цифры 0123456789? д / н ')
    while is_string_valid(is_include_digits) == False:
        print('Ошибка ввода! Введите д или н:')
        is_include_digits = input()

    is_include_lowercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ д / н ')
    while is_string_valid(is_include_lowercase) == False:
        print('Ошибка ввода! Введите д или н:')
        is_include_lowercase = input()

    is_include_uppercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д / н ')
    while is_string_valid(is_include_uppercase) == False:
        print('Ошибка ввода! Введите д или н:')
        is_include_uppercase = input()

    is_include_punctuation = input('Включать ли символы !#$%&*+-=?@^_? д / н ')
    while is_string_valid(is_include_punctuation) == False:
        print('Ошибка ввода! Введите д или н:')
        is_include_punctuation = input()

    if is_include_digits == 'д':
        chars += DIGITS
    if is_include_lowercase == 'д':
        chars += LOWERCASE_LETTERS
    if is_include_uppercase == 'д':
        chars += UPPERCASE_LETTERS
    if is_include_punctuation == 'д':
        chars += PUNCTUATION
    if chars == '':
        print('Ошибка в конфигурации пароля. Необходимо включить как минимум одну группу символов\nПовторите ввод: ')

is_include_symbols = input('Исключать ли неоднозначные символы il1Lo0O? д / н ')
while is_string_valid(is_include_symbols) == False:
    print('Ошибка ввода! Введите д или н:')
    is_include_symbols = input()

if is_include_symbols == 'д':
    for i in range(len(SYMBOLS)):
        chars = chars.replace(SYMBOLS[i], '')

for _ in range(passwords_quantity):
    print(generate_password(password_length, chars))