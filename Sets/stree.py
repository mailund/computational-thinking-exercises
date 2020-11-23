
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

tree = Node(3,
    Node(1, None, Node(2, None, None)),
    Node(7, Node(5, None, None), None)
)
print(len(tree))

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

tree = Node(3,
    Node(1, emptree, Node(2)),
    Node(7, Node(5), emptree)
)
print(len(tree))
