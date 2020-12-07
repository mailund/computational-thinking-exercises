
def parent(j):
    return (j - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2

def fix_down(nodes, n, i):
    while i < n:
        j, k = left(i), right(i)

        if j >= n:
            break # we don't have children, so done

        if k >= n:
            # we have a left child but not a right
            if nodes[i] < nodes[j]:
                nodes[i], nodes[j] = nodes[j], nodes[i]
            break # done

        if nodes[i] >= nodes[j] and nodes[i] >= nodes[k]:
            # children are smaller, so we are done
            break

        # flip with the largest
        if nodes[j] > nodes[k]:
            nodes[i], nodes[j] = nodes[j], nodes[i]
            i = j
        else:
            nodes[i], nodes[k] = nodes[k], nodes[i]
            i = k

def heapsort(x):
    n = len(x)

    # Establish the heap property...
    for i in range(n - 1, -1, -1):
        fix_down(x, n, i)

    # Sort by moving the largest element to the end
    while n > 0:
        # Swap the largest to the end and fix the heap property
        x[n-1], x[0] = x[0], x[n-1]
        fix_down(x, n - 1, 0)
        n -= 1
    return x

print(heapsort([1, 5, 2, 5, 15, 23, 6, 7, 23, 7]))
