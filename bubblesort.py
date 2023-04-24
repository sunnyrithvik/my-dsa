
def bubblesort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(n, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


A = [9, 12, 11, 5, 14, 18, 6, 10, 4, 7, 2, 13, 20, 1, 8]

bubblesort(A)

for i in A:
    print(i, end=' ')
