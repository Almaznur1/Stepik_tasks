'''Дан набор точек на координатной плоскости.
Необходимо подсчитать и вывести количество точек,
лежащих в каждой координатной четверти.
Формат входных данных
B первой строке записано количество точек.
Каждая следующая строка состоит из двух целых чисел —
координат точки (сначала абсцисса - xx, затем ордината - yy),
разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек,
лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат,
не принято относить к какой-либо координатной четверти.'''

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
a, b, c, d = 0, 0, 0, 0
for point in points:
    if point[0] > 0 and point[1] > 0:
        a += 1
    elif point[0] < 0 < point[1]:
        b += 1
    elif point[0] < 0 and point[1] < 0:
        c += 1
    elif point[1] < 0 < point[0]:
        d += 1
print('Первая четверть: ', a)
print('Вторая четверть: ', b)
print('Третья четверть: ', c)
print('Четвертая четверть: ', d)
