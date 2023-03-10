'''
Постулат Бертрана (теорема Бертрана-Чебышева, теорема Чебышева) гласит,
что для любого n > 1 найдется простое число p в интервале n < p < 2n.
Такая гипотеза была выдвинута в 1845 году французским математиком
Джозефем Бертраном (проверившим ее до n=3000000) и доказана в 1850 году
Пафнутием Чебышевым. Рамануджан в 1920 году нашел более простое
доказательство, а Эрдеш в 1932 – еще более простое.

Ваша задача состоит в том, чтобы решить несколько более общую
задачу – а именно по числу n найти количество простых чисел p
из интервала n < p < 2n.

Напомним, что число называется простым,
если оно делится только самона себя и на единицу.

Входные данные
Программа принимает на вход целое число n (2 ≤ n ≤ 50000).

Выходные данные
Вам необходимо вывести на экран одно число – количество простых чисел p
на интервале  n < p < 2n.
'''
n = int(input())
s = 0
for i in range(n + 1, 2 * n):
    flag = True
    for j in range(2, i):
        if j > i ** 0.5:
            break
        if not i % j:
            flag = False
            break
    if flag:
        s += 1
print(s)
