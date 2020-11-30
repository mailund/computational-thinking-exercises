class Leaf(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Node(object):
    def __init__(self, children = ()):
        self.children = list(children)
    def __str__(self):
        children = [str(child) for child in self.children]
        return '({})'.format(','.join(children))

import re
def tokenize(tree):
    return re.findall(r'[()]|\w+', tree)

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

tree = parse("((a,b),c,(d,(e,f)))")
print(tree)
