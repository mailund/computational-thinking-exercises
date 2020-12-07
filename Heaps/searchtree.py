
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


def st_sort(x):
    heap = Heap()
    for e in x:
        heap.insert(e)
    res = []
    while not heap.is_empty():
        res.append(heap.delete_min())
    return res

y = st_sort([5, 1, 3,4, 6, 7])
print(y)