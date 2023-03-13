'''
Наша программа принимает на вход последовательность скобочных символов.
Ваша задача определить является ли введенная скобочная последовательность
правильной.

Правильная скобочная последовательность (ПСП) называется строка, состоящая
только из символов "скобки", где каждой закрывающей скобке найдётся
соответствующая открывающая (причём того же типа). При этом учитывайте, что:

Пустая последовательность является правильной.
Если A – правильная скобочная последовательность,
то (A), [A] и {A} – правильные скобочные последовательности.
Если A и B – правильные скобочные последовательности,
то AB – правильная скобочная последовательность.
Если введенная строка является ПСП, выведите YES, в противном случае - NO.
'''
str = input()
str = [letter for letter in str]
open = ''
openp = '([{'
closep = ')]}'
flag = True
if len(str) % 2:
    flag = False
while len(str) and flag:
    for element in str:
        if element in closep and not open:
            flag = False
            break
        elif element in openp:
            open = element
            continue
        elif element in closep and ord(element) - ord(open) < 3:
            del str[str.index(open)]
            del str[str.index(element)]
            break
        else:
            flag = False
if flag:
    print('YES')
else:
    print('NO')

# вариант со стеком
str = input()
stack = []
openp = '([{'
closep = ')]}'
flag = True
if not len(str) % 2:
    for element in str:
        if element in openp:
            stack.append(element)
        elif ord(element) - ord(stack[-1]) < 3:
            stack.pop()
        else:
            flag = False
            break
else:
    flag = False
if flag:
    print('YES')
else:
    print('NO')