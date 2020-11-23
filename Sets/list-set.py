class ElementNotInSet(Exception):
    pass

class ListSet(object):
    def __init__(self, seq = ()):
        self.data = list(seq)

    def add(self, element):
        if element not in self:
            self.data.append(element)
            i = len(self.data) - 1
            while i > 0 and self.data[i] < self.data[i - 1]:
                self.data[i], self.data[i - 1] = self.data[i - 1], self.data[i]
                i -= 1

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

    def __delitem__(self, element):
        self.remove(element)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, element):
        for x in self.data:
            if x == element:
                return True
        return False

    def __repr__(self):
        return 'ListSet(' + repr(self.data) + ')'


x = ListSet([1, 2, 2, 3, 4, 3, 2])
print(x)
del x[2]
print(x)
del x[3]
print(x)
x.add(0)
x.add(12)
x.add(3)
print(x)
