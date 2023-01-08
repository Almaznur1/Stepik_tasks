'''n человек, пронумерованных числами от 11 до nn, стоят в кругу.
Они начинают считаться, каждый kk-й по счету человек выбывает из круга,
после чего счет продолжается со следующего за ним человека. Напишите программу,
определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа nn и kk, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека,
который останется в кругу последним.'''

n = int(input())
k = int(input())
residue = -1
elements_to_delete = []
arr = [i for i in range(n)]
while k <= len(arr):
    elements_to_delete = [arr[residue + j] for j in range(k, len(arr), k)]
    last_deleted_element_index = arr.index(elements_to_delete[-1])
    residue = len(arr) - last_deleted_element_index - k - 1
    for element in elements_to_delete:
        arr.remove(element)
    print('elements_to_delete= ', *elements_to_delete)
    print('arr= ', *arr)
    print()
# while k > len(arr):
#     residue = len(arr) // k
