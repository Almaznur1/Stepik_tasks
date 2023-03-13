arr = []
b = -3
c = 0
arr.extend(str(int(input())))
if len(arr) > 3:
    for i in range(1, 1 + len(arr) // 3):
        arr.insert(i * b + c, ',')
        c -= 1
    if arr[0] == ',':
        del arr[0]
print(*arr, sep='')