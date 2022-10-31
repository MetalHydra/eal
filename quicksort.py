import random

N = 4
A = [random.randint() for _ in range(N)]
def partition(l:int, r:int):
    p = A[l]
    i = l+1
    j = r

    while j <= i:
        while (i < r) and (A[r] <= p):
            i += 1
        while (j > l) and (A[j] >= p):
            j -= 1
        # swap
        


def quicksort()