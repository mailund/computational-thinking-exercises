
def prod(x, y, z):
    return x * y * z

x = 1
def prod(z):
    y = 2
    return x * y * z

def longest(x, y):
    if len(x) > len(y):
        return x
    else:
        return y


from math import sqrt
def distance(x1, x2, y1, y2):
    return sqrt((x1 - y1)**2 + (x2 - y2)**2)
