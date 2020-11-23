# Sets

## List sets

Consider this implementation of a set:

```python
class ElementNotInSet(Exception):
    pass

class ListSet(object):
    def __init__(self, seq = ()):
        self.data = list(seq)

    def add(self, element):
        if element not in self:
            self.data.append(element)

    def remove(self, element):
        try:
            idx = self.data.index(element)
            self.data = self.data[:idx] + self.data[idx+1:]
        except ValueError:
            raise ElementNotInSet()

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, element):
        for x in self.data:
            if x == element:
                return True
        return False

    def __repr__(self):
        return 'ListSet(' + repr(self.data) + ')'
```

**Exercise:** In `remove()` we copy the entire list except for one element. To get the elements in contiguous memory, we didn’t need to copy the first part of the list, which on average will be half the list if we remove random data. It would be better to only copy the last part of the list. One way to do this is to scan from the beginning towards the end, and once you find the element you want to remove, you start swapping elements. You take the next element and swap it with the one you should delete. Then you swap the next element with the one you want to delete. You continue with this, until you reach the end of the list. Then you can remove the last element with a `pop()`. This way, you will copy half as many elements on average. Implement this idea.

**Answer:**

```python
    def remove(self, element):
        try:
            idx = self.data.index(element)
            for j in range(idx + 1, len(self.data)):
                self.data[j - 1], self.data[j] = self.data[j], self.data[j - 1]
            self.data.pop()
        except ValueError:
            raise ElementNotInSet()
```

A move Pythonic way to delete an element in a list is to use

```python
del x[index]
```

and I would probably have written `remove()` that way if I didn’t want to make the point that the operation requires that you copy elements when you remove something from the middle of a list.

**Answer(wish):** You can implement the `del` operation like

```python
    def __delitem__(self, element):
        self.remove(element)
```

**Exercise:** The previous exercise works if you only have one copy of the element you want to delete. This is the case with our set implementation, but Python’s lists can also handle the general case. Derive a way to delete all occurrences of an element from a list by swapping. You cannot swap one element at a time, but you don’t need to move the element you want to delete upwards at all. It suffices to have an index you need to copy elements to and an index where you need to copy from, and skip past the elements you need to delete. Work out how this can be done, and try to implement your solution.

**Answer:** We can copy elements from a source index `j`, that skips past the element, to a destination index `i`, like this:

```python
    def remove(self, element):
        try:
            i = self.data.index(element)
            for j in range(i + 1, len(self.data)):
                if self.data[j] != element:
                    self.data[i] = self.data[j]
                    i += 1
            for _ in range(len(self.data) - i):
                self.data.pop()
        except ValueError:
            raise ElementNotInSet()
```

**Exercise:** What is the complexity of `add()` with this implementation?

**Answer:** We scan through the list looking at everything after the index we see, and copy the elements there. It is about half the elements, so we have a linear time algorithm. As long as we need a linear time search to find the first element, there is no way around linear time, but we could save even more swapping by swapping occurrences of the element with the last in the list and then popping the occurrence away. Try implementing that.


**Exercise:** The `__contains__()` method is a linear time operation for `ListSet`, but if we used a binary search instead, we could get a logarithmic time operation. That requires, however, that we keep the list sorted when we insert. If you append an element to a sorted list and swap it down until you find its location, similar to how we swap elements down in insertion sort, then you can keep the list sorted with a linear time insertion. Implement this. Does it change the complexity of `add()`, considering that you can only implement `__contains__()` if you keep the list sorted. Explain.

**Answer:**

The implementation can look like this:

```python
    def add(self, element):
        if element not in self:
            self.data.append(element)
            i = len(self.data) - 1
            while i > 0 and self.data[i] < self.data[i - 1]:
                self.data[i], self.data[i - 1] = self.data[i - 1], self.data[i]
                i -= 1
```

The complexity is the same as before. Before we insert, we do a linear search, so we pay a linear time cost there. Swapping the element down to get a sorted list doesn't cost us more than linear time on top of that.


## Search trees

**Exercise:** Why would a balanced tree have max depth in O(log n)?

**Answer:** If the tree is balanced, half the nodes in a tree are in the left tree and the other in the right. If we go left or right, we have eliminated half the tree. If we divide the tree by half in each step as we go down, we get a logarithmic depth.

**Exercise:** With a search tree, you can also find the minimal and maximal element in a set in time proportional to the height of the tree. Write functions that do this.

```python
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def min_val(self):
        if self.left is None:
            return self.val
        else:
            return self.left.min_val()

    def max_val(self):
        if self.right is None:
            return self.val
        else:
            return self.right.max_val()
```

**Exercise:** How would you implement the `__len__()` method for the search tree?

**Answer:** You can write a recursive function that you can use in the method:

```python

def tree_size(n):
    if n is None: return 0
    else: return tree_size(n.left) + 1 + tree_size(n.right)

class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __len__(self):
        return tree_size(self)
```

You can also create a dummy class for empty trees, so you can call the `__len__()` method on empty trees. In searches, that I haven't shown here, you would have to check if the empty tree is this object rather than `None`, but otherwise there is not much difference.

```python
class Empty(object):
    def __len__(self):
        return 0

emptree = Empty()

class Node(object):
    def __init__(self, val, left = emptree, right = emptree):
        self.val = val
        self.left = left
        self.right = right

    def __len__(self):
        return len(self.left) + 1 + len(self.right)
```


**Exercise:** Why is sorted or reverse-sorted data the worst case scenario when building a search tree?

## Hash tables

Take this implementation of a hash table:

```python
def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power

class HashTableSet(object):
    def __init__(self, seq = (), initial_size = 16):
        seq = list(seq)

        if 2 * len(seq) > initial_size:
            initial_size = next_power_of_two(2 * len(seq))

        self.size = initial_size
        self.used = 0
        self.array = [list() for _ in range(initial_size)]

        for value in seq:
            self.add(value)

    def get_bin(self, element):
        hash_val = hash(element)
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for x in bin:
                self.add(x)

    def add(self, element):
        bin = self.get_bin(element)
        if element not in bin:
            bin.append(element)
            self.used += 1
            if self.used > self.size / 2:
                self.resize(int(2 * self.size))

    def remove(self, element):
        bin = self.get_bin(element)
        if element not in bin:
            raise ElementNotInSet()
        bin.remove(element)
        self.used -= 1
        if self.used < self.size / 4:
            self.resize(int(self.size / 2))

    def __iter__(self):
        for bin in self.array:
            yield from bin

    def __contains__(self, element):
        bin = self.get_bin(element)
        return element in bin

    def __repr__(self):
        return 'HashTableSet(' + repr(list(iter(self))) + ')'
```

I wanted my size to be powers of two, because it can be more efficient to extract lower bits than compute modulo, but in the implementation I do use modulo, so it isn’t strictly necessary to round up in the constructor. I do it anyway, in case I later decide to use the bit-manipulation version for the mapping.

**Exercise:** Implement the `__len__()` method for the set.

**Answer:**

We want the number of elements in the set, which we have in the `used` attribute.

```python
    def __len__(self):
        return self.used
```

**Exercise:** When we resize, we recompute the hash values for all objects. Computing the hash value might be an expensive operation, and the value never changes for an object, so it seems wasteful. Can you update the implementation so you save the hash value together with the object, and use when you resize? You still need to do the bin mapping, of course, but reuse the hash value.

**Answer:** You have to store pairs of elements and hash values. It will look something like the code below (but be careful, I haven't tested it rigoursly).

```python
def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power

class HashTableSet(object):
    def __init__(self, seq = (), initial_size = 16):
        seq = list(seq)

        if 2 * len(seq) > initial_size:
            initial_size = next_power_of_two(2 * len(seq))

        self.size = initial_size
        self.used = 0
        self.array = [list() for _ in range(initial_size)]

        for value in seq:
            self.add(value)

    def get_bin(self, hash_val):
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for (element,h) in bin:
                bin = self.get_bin(h)
                bin.append((element,h))
                self.used += 1

    def add(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        if (element,h) not in bin:
            bin.append((element,h))
            self.used += 1
            if self.used > self.size / 2:
                self.resize(int(2 * self.size))

    def remove(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        if (element,h) not in bin:
            raise ElementNotInSet()
        bin.remove((element,h))
        self.used -= 1
        if self.used < self.size / 4:
            self.resize(int(self.size / 2))

    def __iter__(self):
        for bin in self.array:
            yield from (element for (element,h) in bin)

    def __contains__(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        return (element,h) in bin

    def __repr__(self):
        return 'HashTableSet(' + repr(list(iter(self))) + ')'

    def __len__(self):
        return self.used
```

## Dictionary

This is how you could implement a dictionary using a hash table:

```python

def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power

def get_bin_index(bin, key):
    for i, (k, v) in enumerate(bin):
        if k == key:
            return i
    return None

class HashTableDict(object):
    def __init__(self, seq = (), initial_size = 16):
        seq = list(seq)

        if 2 * len(seq) > initial_size:
            initial_size = next_power_of_two(2 * len(seq))

        self.size = initial_size
        self.used = 0
        self.array = [list() for _ in range(initial_size)]

        for key, val in seq:
            self[key] = val

    def get_bin(self, key):
        hash_val = hash(key)
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for (key,val) in bin:
                self[key] = val

    def __setitem__(self, key, value):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            bin.append((key, value))
            self.used += 1
            if self.used > self.size / 2:
                self.resize(2 * self.size)
        else:
            bin[idx] = (key, value)

    def __getitem__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            raise KeyError(key)
        else:
            k, v = bin[idx]
            return v

    def __delitem__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            raise KeyError(key)
        else:
            del bin[idx]
            self.used -= 1
            if self.used < self.size / 4:
                self.resize(int(self.size / 2))

    def __contains__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        return idx is not None

    def __iter__(self):
        for bin in self.array:
            yield from bin

    def __repr__(self):
        return 'HashTableDict(' + repr(list(iter(self))) + ')'
```

You can use it like this:

```python
table = HashTableDict([("foo", 1), ("bar", 2), ("baz", 3)])

del table["bar"]
table["foo"] = 12
table["qux"] = 21

if "foo" in table:
    print(table["qux"])

for key in table:
    print(key, "->", table[key])
```

The comments show which magical method each operation uses.

**Exercise:** Take this `list` implementation of a set and change it into a dictionary:

```python
class ElementNotInSet(Exception):
    pass

class ListSet(object):
    def __init__(self, seq = ()):
        self.data = list(seq)

    def add(self, element):
        if element not in self:
            self.data.append(element)

    def remove(self, element):
        try:
            idx = self.data.index(element)
            self.data = self.data[:idx] + self.data[idx+1:]
        except ValueError:
            raise ElementNotInSet()

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, element):
        for x in self.data:
            if x == element:
                return True
        return False

    def __repr__(self):
        return 'ListSet(' + repr(self.data) + ')'
```

**Answer:**

```python
class ListDict(object):
    def __init__(self, seq = ()):
        self.data = list(seq)

    def __setitem__(self, key, value):
        for i,(k,v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def __getitem__(self, key):
        for k,v in self.data:
            if k == key: return v
        raise KeyError(key)

    def __delitem__(self, key):
        for i,(k,v) in enumerate(self.data):
            if k == key:
                self.data.pop(i)
                return
        raise KeyError(key)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, element):
        for x in self.data:
            if x == element:
                return True
        return False

    def __repr__(self):
        return 'ListSet(' + repr(self.data) + ')'
```
