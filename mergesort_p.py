
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    leftsort = mergesort(left)
    rightsort = mergesort(right)

    a = []
    i = j = 0
    while i < len(leftsort) and j < len(rightsort):
        if leftsort[i] <= rightsort[j]:
            a.append(leftsort[i])
            i = i + 1
        else:
            a.append(rightsort[j])
            j = j + 1

    a.extend(leftsort[i:])
    a.extend(rightsort[j:])

    return a


arr = [5, 9, 3, 7, 1, 6, 2, 0]
print(arr)
arry = mergesort(arr)
print(arry)
