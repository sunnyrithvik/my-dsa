import time

start_time = time.time()


def merge(A, p, q, r):
    nl = q-p+1
    nr = r-q

    L = [0]*nl
    R = [0]*nr

    for i in range(0, nl):
        L[i] = A[p+i]

    for j in range(0, nr):
        R[j] = A[q+j+1]

    i = 0
    j = 0
    k = p

    while i < nl and j < nr:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
        k = k+1

    while i < nl:
        A[k] = L[i]
        i = i+1
        k = k+1
    while j < nr:
        A[k] = R[j]
        j = j+1
        k = k+1


def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2

        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)


A = [9, 12, 11, 5, 14, 18, 6, 10, 4, 7, 2, 13, 20, 1, 8]
n = len(A)
print("size", n)

mergesort(A, 0, n-1)

for i in A:
    print(i, end=' ')


end_time = time.time()
duration = end_time - start_time

print("Duration: ", duration)
