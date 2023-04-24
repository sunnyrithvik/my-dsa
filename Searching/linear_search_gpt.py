def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [3, 5, 2, 8, 1]
x = 8
result = linear_search(arr, x)
if result == -1:
    print("Value not found in array")
else:
    print(f"Value found at index {result}")
