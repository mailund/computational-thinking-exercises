
import numpy.random as ran

def partition(x, i, j):
    """
    Let pivot = x[i]. This function will
    arrange x[i:j] into x'[i:k] + x'[k:j] such that
    x'[h] <= pivot for h = i ... k and
    x'[k] == pivot and
    x'[h] > pivot for h = k + 1 ... j
    and then returns this k
    """
    pivot = x[i]
    k, h = i + 1, j - 1
    while k <= h:
        if x[k] == pivot:
            k += 1
        elif x[k] < pivot:
            x[k], x[k - 1] = x[k - 1], x[k]
            k += 1
        elif x[k] > pivot:
            x[k], x[h] = x[h], x[k]
            h -= 1
    return k - 1 # - 1 because k always points one *past* pivot


def check_partition(x, k, pivot):
    if not all(x[h] <= pivot for h in range(k)):
        print("prefix is not correct")
        print(x, x[:k], x[k], x[k+1:])
    if not x[k] == pivot:
        print("k is not correct")
        print(x, x[:k], x[k], x[k+1:])
    if not all(x[h] > pivot for h in range(k+1, len(x))):
        print("post fix is not correct")
        print(x, x[:k], x[k], x[k+1:])

print("testing partitioning")
for i in range(10):
    x = list(ran.random_integers(0, size = 10, high = 10))
    print(x)
    pivot = x[0]
    k = partition(x, 0, len(x))
    check_partition(x, k, pivot)


def qsort(x, i, j):
    if j - i <= 1: 
        return  # x[i:j] is [] or [e] -> so already sorted
    
    k = partition(x, i, j)
    qsort(x, i, k)
    qsort(x, k + 1, j)

print("testing sorting")
for i in range(10):
    x = list(ran.random_integers(0, size = 10, high = 10))
    print(x)
    y = x[:]
    qsort(y, 0, len(x))
    print(y)
    if sorted(x) != y:
        print("not sorted!")

def qsort_tr(x, i, j):
    while True:
        if j - i <= 1: 
            return  # x[i:j] is [] or [e] -> so already sorted
    
        k = partition(x, i, j)
        qsort_tr(x, i, k)
        #qsort_tr(x, k + 1, j)
        i = k + 1

print("testing tail-recursive sorting")
for i in range(10):
    x = list(ran.random_integers(0, size = 10, high = 10))
    print(x)
    y = x[:]
    qsort_tr(y, 0, len(x))
    print(y)
    if sorted(x) != y:
        print("not sorted!")



def qsort_tr(x, i, j):
    while True:
        if j - i <= 1: 
            return  # x[i:j] is [] or [e] -> so already sorted
    
        k = partition(x, i, j)
        # recursing on the smallest interval, tail-recursing on largest
        if i - k > j - (k + 1):
            qsort_tr(x, k + 1, j)
            #qsort_tr(x, i, k)
            j = k
        else:
            qsort_tr(x, i, k)
            #qsort_tr(x, k + 1, j)
            i = k + 1

print("testing tail-recursive sorting")
for i in range(10):
    x = list(ran.random_integers(0, size = 10, high = 10))
    print(x)
    y = x[:]
    qsort_tr(y, 0, len(x))
    print(y)
    if sorted(x) != y:
        print("not sorted!")

