import random

def get_word(list):
   return random.choice(list)

def is_valid_input(str, word_len):
   return str.isalpha() and len(str) == word_len or str.isalpha() and len(str) == 1

def play(word):
    word_completion = ['_' for i in range(len(word))]  # список, содержащий символы _ на каждую букву задуманного слова
    tries = 6                                          # количество попыток
    word_letters_list = []
    word_letters_list.extend(word)
    print('Давайте играть в угадайку слов!')
    while tries != 0:
        print(display_hangman(tries))
        print(*word_completion)        
        player_input = input('Введите букву или слово\n')
        while is_valid_input(player_input, len(word)) == False:
            print(f'Ошибка ввода!\nВведите букву или слово ({len(word)} букв(ы))')
            player_input = input()  
        if len(player_input) == 1:                                    # если введена одна буква
            if player_input in word:
                for i in range(len(word)):
                    if word_letters_list[i] == player_input:
                        word_completion[i] = player_input
                print('Отлично, вы угадали букву!')
            else:
                tries -= 1
                print('Ошибка! Осталось попыток:', tries)
        elif len(player_input) == len(word):                           # если введено слово
            if player_input == word:
                print('Поздравляем, вы угадали слово!')
                return word
            else:
                tries -= 1
                print('Ошибка! Осталось попыток:', tries)                
        if word_completion == word_letters_list:
            print('Поздравляем, вы угадали слово!')
            return word
        if tries == 0:
            print(display_hangman(tries))
            print(f'Вы не смогли угадать слово. Загаданное слово:\n{word}')
            return

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

word_list = ['car', 'star', 'mirror', 'city', 'weather', 'flat', 'computer', 'wheat', 'bread', 'danger']
guessed_words = []
c = 'y'
while c == 'y':
    guessed_word = play(get_word(word_list))
    word_list.remove(guessed_word)
    guessed_words.append(guessed_word)
    print('Угаданные слова: ', *guessed_words)
    c = input('Хотите сыграть еще раз? y / n ')