# Heaps

## Search trees

**Exercise:** Implement a heap using a search tree.

**Answer**

```python
## Search tree implementation...
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Node({self.val},{self.left},{self.right})"
    __str__ = __repr__

def st_add(st, val):
    if st is None:    return Node(val)
    if st.val == val: return st
    if val < st.val:  return Node(st.val, st_add(st.left, val), st.right)
    else:             return Node(st.val, st.left, st_add(st.right, val))

def rightmost_val(st):
    while st.right is not None:
        st = st.right
    return st.val

def st_remove(st, val):
    if st is None:     return None
    if val < st.val:   return Node(st.val, st_remove(st.left, val), st.right)
    elif val > st.val: return Node(st.val, st.left, st_remove(st.right, val))

    assert st.val == val
    if st.left is None:  return st.right
    if st.right is None: return st.left
    rmval = rightmost_val(st)
    return Node(rmval, st_remove(st.left, rmval), st.right)

## Heap implementation
class Heap(object):
    def __init__(self):
        self.st = None

    def insert(self, val):
        self.st = st_add(self.st, val)

    def get_min(self):
        st = self.st
        while st.left is not None:
            st = st.left
        return st.val

    def delete_min(self):
        val = self.get_min()
        self.st = st_remove(self.st, val)
        return val

    def is_empty(self):
        return self.st is None
```

**Exercise:** Implement a sort algorithm based on it.

**Answer:**

```python
def st_sort(x):
    heap = Heap()
    for e in x:
        heap.insert(e)
    res = []
    while not heap.is_empty():
        res.append(heap.delete_min())
    return res
```


**Exercise:** If you have two search trees, where all elements in the first are smaller than all elements in the second, can you merge them smarter than if they do not have this property? What would the complexity be?

**Answer:** You can get the largest (rightmost) value in the first tree, and delete it from the first tree. Then you can make a new root of both trees, with that value, and with the (modified) first tree as its left subtree and the other tree as its right subtree. The complexity is the time it takes to find and remove the right most value, i.e., O(log n).

## Binary heaps

**Exercise:** If we have inserted and deleted many times, the smaller values will likely be closer to the root, so when we pull out a value from the lowest level and let it fall down through the layers, it mostly ends near the bottom once again. When we `fix_down()` we compare a node with both its children at each level, which is two comparisons. We could also do a single comparison and figure out which of the children is smallest and swap the value with its smaller child, *without* caring whether it is already smaller than this child. This way, we would swap it all the way down to the lowest layer—in the neighbourhood where it probably belongs anyway. Since we might have taken it too far, we can try to fix it upwards again after that. Here, we make one comparison per level, but we will get it as high as it has to go. Under which circumstances is one approach preferable to the other?

**Answer:** We can consider the path along which we would swap the value down the heap. Let us call it `d`. In the first approach, we do two comparisons at each level, but we stop when we get the right position, so we spend time `2d`. If we always swap with the smaller child, we continue past `d` down to the bottom level. Call the extra path `e`. Then we swap back up again along that path. So there, we would spend time `1d + 2e`. Thus, the former is better if `e > 1/2d` and the latter is better otherwise.


## Heap sort with binary heap

You can implement a heap sort using a binary heap where you do not use any extra memory—you can do all the operations in the input list.

1. Build the heap from the list, which means rearrange the lists via `fix_down()`.
2. Apply `delete_min()` `n` times (just throw away the result, you don’t need it; you put it at the end of the list. You have to keep the list elements around, though, so you cannot `pop()` the last element, and you cannot use the list’s length to tell you how many elements you have in the heap.
3. After you are done, all the elements are sorted in reverse order—reverse the list and you are done.

**Exercise:** Explain why the elements are sorted in reverse order after you have deleted all the elements in the heap.

**Answer:** When we `delete_min()`, we move the smallest element to the end of the (current) list. When we iteratively do this, we move the elements there in increasing order, but at the position just behind those we have already inserted there. When the heap is empty, we have moved all the elements, but the smallest ended up furthest from the beginning.

**Exercise:** Change the heap implementation so you delete the maximum, not the minimum, element. That way you do not need to reverse the list at the end.

**Answer:**

```python
def parent(j):
    return (j - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2

# Fix down in a max-heap
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
```
