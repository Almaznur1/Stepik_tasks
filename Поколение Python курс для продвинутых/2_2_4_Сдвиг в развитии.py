'''На вход программе подается строка текста из натуральных чисел.
Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо,
когда последний элемент становится первым,
а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

Формат входных данных
На вход программе подается строка текста
из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести элементы измененного списка с циклическим сдвигом,
разделяя его элементы одним пробелом.'''

arr = [int(n) for n in input().split()]
arr = [arr[i - 1] for i in range(len(arr))]
print(*arr)