# Stacks and queues

## Reverse Polish notation

**Exercise:** Translate the following expressions into reverse Polish notation:
* `(1 + 3) * (4 - 1)`
* `~1 * (3 * 4 / 5)`
* `(1 + (2 + 3)) * 3`
* `1 + 2 + 3 * 3`

**Answer:**
* `1 3 + 4 1 - *`
* `1 ~ 3 4 * 5 / *`
* `1 2 3 + + 3 *`
* `1 2 + 3 3 * +`

**Exercise:** Write down the stack for each step in the evaluation

**Answer:** I will do the first, you will do the rest...

```
push 1: [] => [1]
push 3: [1] => [1, 3]
op +:   [1, 3] => [4]
push 4: [4] => [4, 4]
push 1: [4, 4] => [4, 4, 1]
op -:   [4, 4, 1] => [4, 3]
op *:   [4, 3] => [12]
```

## Linked list stack

You can easily build a stack from singly-linked lists. Recall that a link is defined this way:

```python
class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
```

**Exercise:** Implement a stack by filling in the blanks in the code below:

```python
class Stack(object):
    def __init__(self):
        # code here

    def push(self, x):
        # code here

    def top(self):
        # code here

    def pop(self):
        # code here

    def is_empty(self):
        # code here
```

**Answer:**

```python
class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next

class Stack(object):
    def __init__(self):
        self.stack = None

    def push(self, x):
        self.stack = Link(x, self.stack)

    def top(self):
        # You could check for errors here if you want
        self.stack.element

    def pop(self):
        # You could check for errors here if you want
        res = self.stack.element
        self.stack = self.stack.next
        return res

    def is_empty(self):
        return self.stack is None
```

## Parsing Newick trees

The Newick tree file format represents trees in a text with nested parentheses. You can specify branch lengths and similar annotations, but here we will just assume that a tree is either a simple alpha-numeric string, which we consider a leaf, or it is a list of comma-separated trees surrounded by parentheses. Something like this:

```
tree = '(A, (B, C))'
```

In this exercise, we will parse such trees and build a tree of them, represented with classes:

```python
class Leaf(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Node(object):
    def __init__(self, children = ()):
        self.children = listl(children)
    def __str__(self):
        children = [str(child) for child in self.children]
        return '({})'.format(','.join(children))
```

Dealing with raw text when you want to parse something is usually a bad idea. The first step you always do is that you translate the text into a list of “tokens”, i.e., a list of the meaningful parts of the string. While it isn’t completely safe, you can use this function for the exercise:

```python
import re
def tokenize(tree):
    return re.findall(r'[()]|\w+', tree)
```

It turns the string `(A,(B,C))` into `['(', 'A', '(', 'B', 'C', ')', ')']`.

Here is the idea for parsing the tree:
1. Whenever you see a token that isn’t `)`, push it on the stack.
2. If you see a token that is neither `(` or `)` it must be a leaf, so create a leaf and push it to the stack.
3. When you see `)`, iteratively pop trees from the stack and collect them in a list. When you reach the first `(` you stop popping, you create the new tree, and you push it on the stack.

**Exercise:** Implement a Newick parser based on this idea.

**Answer:**

```python
def parse(newick):
    tokens = tokenize(newick)
    stack = [Node()]
    for tok in tokens:
        if tok == '(':
            stack.append(Node())
        elif tok == ')':
            tree = stack.pop()
            stack[-1].children.append(tree)
        else:
            stack[-1].children.append(Leaf(tok))
    assert len(stack) == 1, "There should only be one node left now"
    return stack.pop()
```

**Exercise:** If you take the tree `((A,B),C,((D,E),F))`, in which order will your algorithm created `Leaf`s and `Node`s?

**Answer:** You build the inner nodes before their children, and put them on the stack. Then you add them to their parents when you pop them.


## Doubly-linked queue

A link in a doubly-linked list looks like this:

```python
class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.prev = previous
        self.next = next
```

**Exercise:** Implement a queue using doubly-linked lists by filling in the blanks in the code below:

```python
class Queue(object):
    def __init__(self):
        # code here

    def is_empty(self):
        # code here

    def enqueue(self, x):
        # code here

    def front(self):
        # code here

    def dequeue(self):
        # code here
```

This is easiest if you add a dummy element at the beginning and end of the list (but you can make it the same dummy without any problems—and probably without changing any code except the constructor).

**Answer:**

```python
class Queue(object):
    def __init__(self):
        self.head = DoublyLink(None, None, None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        return self.head.next == self.head

    def enqueue(self, x):
        # Put the new link at the end of the queue, i.e.
        # just before head
        link = DoublyLink(x, self.head.prev, self.head)
        link.prev.next = link ; link.next.prev = link

    def front(self):
        return self.head.next.element

    def dequeue(self):
        # Remove the front link and return its value
        val = self.head.next.element
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
```
