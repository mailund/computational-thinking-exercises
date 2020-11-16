
class ListIndexError(Exception):
    pass

class ListSequence(object):
    def __init__(self):
        self.sequence = []
    def append(self, element):
        self.sequence.append(element)

    def get_at_index(self, index):
        try:
            return self.sequence[index]
        except IndexError:
            raise ListIndexError()

    def set_at_index(self, index, value):
        try:
            self.sequence[index] = value
        except IndexError:
            raise ListIndexError()

    def __repr__(self):
        return repr(self.sequence)

seq = ListSequence()
seq.get_at_index(0)     # => IndexError
seq.set_at_index(0, 42) # => IndexError

seq.append(0)
# now these are fine
seq.get_at_index(0) # => IndexError
seq.set_at_index(0, 42) # => IndexError
