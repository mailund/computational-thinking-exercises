# Sequences

## Exceptions

Using Python’s builtin list type, we can implement this interface like this:

```python
class ListSequence(object):
    def __init__(self):
        self.sequence = []
    def append(self, element):
        self.sequence.append(element)
    def get_at_index(self, index):
        return self.sequence[index]
    def set_at_index(self, index, value):
        self.sequence[index] = value
    def __repr__(self):
        return repr(self.sequence)
```

**Exercise:** Create an instance of a `ListSequence` and call `get_at_index()` and `set_at_index()` with invalid input to see which exceptions you get.

If we want implementations of the `Sequence` abstract data type to be replaceable, they should have the same exception. Define and implement an exception, then use it for these class’s methods (catch exceptions and raise your new class).

## Single linked lists

This is a link for a single-linked lists:

```python
class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
    def __repr__(self):
        return 'Link({}, {})'.format(
            self.element,
            repr(self.next)
        )
```

You can create lists using e.g.

```python
Link(21, Link(43, None))
```

and always prepend a value `val` to a list `lst` using 

```python
new_lst = Link(al, lst)
```

**Exercise:** To get a feeling for how you would write recursive functions on a list, try implementing a function, `drop()`, that removes `k` elements from a list, i.e., a function that returns a new list that contains all the elements from a list except the first `k`.

**Exercise:** Write a function, `take()`, that creates a list of only the first `k` elements of a list.

**Exercise:** Write a function, `reverse()`, that reverses a linked list. The easiest way to do this is to add an accumulator to your function that constructs the new list. For each link you recurse on, you can prepend to that accumulator. When you reach the end of the list, you can return the accumulated list.

**Exercise:** Write a function that makes a copy of a linked list.

## Manipulating doubly linked lists

Doubly-linked lists are defined as:

```python
class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.previous = previous
        self.next = next

class DoublyLinkedListSequence(object):
    def __init__(self):
        self.first = DoublyLink(None, None, None)
        self.last = DoublyLink(None, None, None)
        self.first.next = self.last
        self.last.previous = self.first
```

We can insert a new link after a link we have a reference to using

```python
def insert_after(link, element):
    new_link = DoublyLink(element, link, link.next)
    new_link.previous.next = new_link
    new_link.next.previous = new_link
```

**Exercise:** Draw a list and an insertion and convince yourself that this will work.

We can remove a link using

```python
def remove_link(link):
    link.previous.next = link.next
    link.next.previous = link.previous
```

**Exercise:** Draw a list and a removal and convince yourself that this will work.

## Circular lists

This is a complete implementation of doubly-linked lists with dummy elements at the ends.

```python
def insert_list_after(link, begin, end):
    end.next = link.next
    end.next.previous = end
    begin.previous = link
    link.next = begin

def insert_after(link, element):
    new_link = DoublyLink(element, None, None)
    insert_list_after(link, new_link, new_link)

def remove_link(link):
    link.previous.next = link.next
    link.next.previous = link.previous

class DoublyLinkedListSequence(object):
    def __init__(self):
        self.first = DoublyLink(None, None, None)
        self.last = DoublyLink(None, None, None)
        self.first.next = self.last
        self.last.previous = self.first

    def append(self, element):
        insert_after(self.last.previous, element)

    def prepend(self, element):
        insert_after(self.first, element)

    def get_at_index(self, index):
        return self.get_link(index).element

    def set_at_index(self, index, value):
        self.get_link(index).element = value

    def extend(self, other):
        insert_list_after(self.last.previous,
                          other.first.next,
                          other.last.previous)

    def insert_sequence_at(self, index, other):
        link = self.get_link(index)
        insert_list_after(link,
                          other.first.next,
                          other.last.previous)

    def remove_first(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.first.next)

    def remove_last(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.last.previous)

    def remove_first(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.first.next)

    def remove_last(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.last.previous)

    def __repr__(self):
        return repr(self.first.next)
```

**Exercise:** We have a first and last dummy element now, but we never have anything before the first dummy or after the last dummy, so we could combine the two dummies into one. The real elements start at the next reference of the dummy and ends when the next reference is the dummy again. Such a structure is called a *circular* list. Change the implementation to use a circular list (you need to change *very* little).

