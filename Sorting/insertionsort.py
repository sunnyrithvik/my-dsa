def insertionsort(A):
    for i in range(2, len(A)):
        key = A[i]
        j = i-1

        while (j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key


A = [9, 12, 11, 5, 14, 18, 6, 10, 4, 7, 2, 13, 20, 1, 8]
insertionsort(A)

for i in A:
    print(i)
