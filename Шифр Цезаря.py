RU_LOWER = ('абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя')
RU_UPPER = ('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
EN_LOWER = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
EN_UPPER = ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
def is_valid_input(str):
    return str == '1' or str == '2'

def is_valid_shag(str, lang):
    return str.isdigit() and (0 < int(str) < 33 and lang == '1' or 0 < int(str) < 26 and lang == '2')

def encrypt(word, direction, lang, shag):
    result = list(word)
    if direction == '2':
        shag *= -1
    if lang == '1':
        for i in range(len(word)):
            if RU_LOWER.find(word[i]) > -1:
                result[i] = RU_LOWER[RU_LOWER.find(word[i]) + shag]
            if RU_UPPER.find(word[i]) > -1:
                result[i] = RU_UPPER[RU_UPPER.find(word[i]) + shag]            
    if lang == '2':
        for i in range(len(word)):
            if EN_LOWER.find(word[i]) > -1:
                result[i] = EN_LOWER[EN_LOWER.find(word[i]) + shag]
            if EN_UPPER.find(word[i]) > -1:
                result[i] = EN_UPPER[EN_UPPER.find(word[i]) + shag]
    return result
word = input('Введите слово:\n')
direction = input('Выберите напрвление:\n1. Шифрование.\n2. Дешифрование.\n')
while is_valid_input(direction) == False:
    direction = input('Ошибка ввода! Введите цифру 1 или 2\nВыберите напрвление:\n1. Шифрование.\n2. Дешифрование.\n')
lang = input('Выберите язык:\n1. Русский\n2. Английский\n')
while is_valid_input(lang) == False:
    lang = input('Ошибка ввода! Введите цифру 1 или 2\nВыберите язык:\n1. Русский\n2. Английский\n')
shag = input('Укажите шаг сдвига:\n')
while is_valid_shag(shag, lang) == False:
    shag = input('Ошибка ввода! Введите шаг (от 1 до 32 для русского алфавита и от 1 до 25 для английского алфавита)\nУкажите шаг сдвига:\n')

print(*encrypt(word, direction, lang, int(shag)), sep='')