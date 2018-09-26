
# coding: utf-8

# # Hybrid sorting
# 
# 

# In[52]:


import numpy as np
import numpy.random as ran
from timeit import default_timer as timer
#import panda as pd
#import seaborn as sns


# In[2]:


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
        if x[k] <= pivot:
            k += 1
        elif x[k] > pivot:
            x[k], x[h] = x[h], x[k]
            h -= 1

    # If the last in the first partion is not pivot,
    # then make sure that it is.
    last_less = k - 1  # - 1 because k always points one *past* pivot
    if x[last_less] != pivot:
        x[i], x[last_less] = x[last_less], x[i]

    return last_less


# In[3]:


def qsort_rec(x, i, j):
    while True:
        if j - i <= 1: 
            return  # x[i:j] is [] or [e] -> so already sorted
    
        k = partition(x, i, j)
        # recursing on the smallest interval, tail-recursing on largest
        if i - k > j - (k + 1):
            qsort_rec(x, k + 1, j)
            #qsort(x, i, k)
            j = k
        else:
            qsort_rec(x, i, k)
            #qsort(x, k + 1, j)
            i = k + 1


def qsort(x):
    qsort_rec(x, 0, len(x))


# In[5]:


def insertion_sort(x):
    for i in range(1,len(x)):
        j = i
        while j > 0 and x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            j -= 1


# In[8]:


def builtin(x):
    x.sort()


# In[110]:

def time_algorithms(ns, sort_algs):
    time_results = {'alg': [], 'n': [], 'time': []}
    for n in ns:
        x = list(ran.randint(10, size = n))
        for alg in sort_algs:
            x_copy = x[:]
            start = timer()
            alg(x_copy)
            end = timer()
            time_results['alg'].append(alg.__name__)
            time_results['n'].append(5) # <- infinite loop if I do this
            time_results['time'] = end - start
            assert sorted(x) == x_copy
    return time_results

no_reps = 5
min_n, max_n = 1, 5
algs = [builtin, qsort, insertion_sort]
ns = []
for n in range(min_n, max_n):
    ns.extend([n] * no_reps)
print(ns)
time_measures = time_algorithms(ns, algs)
print(time_measures)

