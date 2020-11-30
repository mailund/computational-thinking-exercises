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
