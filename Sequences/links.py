class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
    def __repr__(self):
        return 'Link({}, {})'.format(
            self.element,
            repr(self.next)
        )

lst = None
for i in reversed(range(10)):
    lst = Link(i, lst)
print(lst)


def drop(x, k):
    # if x is too short, you get None
    # alternatively, raise an exception
    if x is None or k == 0: return x
    else: return drop(x.next, k - 1)

def take(x, k):
    # if x is too short, you get None
    # alternatively, raise an exception
    if x is None or k == 0: return None
    else: return Link(x.element, take(x.next, k - 1))

def reverse(x, acc = None):
    if x is None: return acc
    else: return reverse(x.next, Link(x.element, acc))

def copy(x):
    if x is None: return None
    else: return Link(x.element, copy(x.next))

print(drop(lst, 2))
print(take(lst, 5))
print(reverse(lst))
print(copy(lst))
