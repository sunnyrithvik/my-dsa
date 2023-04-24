def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 3, 5, 7, 9]
x = 7
result = binary_search(arr, x)
if result == -1:
    print("Value not found in array")
else:
    print(f"Value found at index {result}")
