EN_LOWER = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
EN_UPPER = ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')

def encrypt(word):
    result = []
    arr = []
    arr = word.split()
    for i in range(len(arr)):
        word_length = [arr[i][k] for k in range(len(arr[i])) if arr[i][k].isalpha()]
        for j in range(len(arr[i])):
            if EN_LOWER.find(arr[i][j]) > -1:          
                result.append(EN_LOWER[EN_LOWER.find(arr[i][j]) + len(word_length)])
            elif EN_UPPER.find(arr[i][j]) > -1:        
                result.append(EN_UPPER[EN_UPPER.find(arr[i][j]) + len(word_length)])
            else:
                result.append(arr[i][j])
    while word.find(' ') > -1:
        result.insert(word.find(' '), ' ')
        word = word.replace(' ', '.', 1)
    return ''.join(result) 

word = input('Введите слово:\n')
print(*encrypt(word), sep='')