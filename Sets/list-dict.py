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

x = ListDict([("foo", 1), ("bar", 2), ("baz", 3)])
print(x)
x['bar'] = 42
x['qux'] = 13
print(x['bar'])
print(x)
del x['foo']
print(x)
