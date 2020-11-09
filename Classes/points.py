
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


p1 = Point(1, 0)
p2 = Point(0, 1)

print(p1 + p2)

print(p1 + p2 - p1)
