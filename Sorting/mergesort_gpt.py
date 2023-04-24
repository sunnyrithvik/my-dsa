
import time

start_time = time.time()

# faster than normal mergesort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = []
    i = j = 0
    while i < len(left_half_sorted) and j < len(right_half_sorted):
        if left_half_sorted[i] < right_half_sorted[j]:
            sorted_arr.append(left_half_sorted[i])
            i += 1
        else:
            sorted_arr.append(right_half_sorted[j])
            j += 1

    sorted_arr.extend(left_half_sorted[i:])
    sorted_arr.extend(right_half_sorted[j:])

    return sorted_arr


# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
arr = [9, 12, 11, 5, 14, 18, 6, 10, 4, 7, 2, 13, 20, 1, 8]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


end_time = time.time()
duration = end_time - start_time

print("Duration: ", duration)
