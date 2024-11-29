def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    bubble_sort_recursive(arr, n - 1)

data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum Disorting:")
print(data)

bubble_sort_recursive(data)

print("List Yang Sudah Disorting:")
print(data)
