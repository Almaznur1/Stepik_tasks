n = int(input())
k = int(input())
residue = 0
deleted_elements = []
arr = [i for i in range(n)]

list_start = k - 1
for i in range(len(arr) // k):
    deleted_elements.append(arr[i * k + list_start])
print(*arr)
print(*deleted_elements)
for i in range(len(deleted_elements)):
    arr.remove(deleted_elements[i])
print(*arr)