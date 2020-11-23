def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power

class HashTableSet(object):
    def __init__(self, seq = (), initial_size = 16):
        seq = list(seq)

        if 2 * len(seq) > initial_size:
            initial_size = next_power_of_two(2 * len(seq))

        self.size = initial_size
        self.used = 0
        self.array = [list() for _ in range(initial_size)]

        for value in seq:
            self.add(value)

    def get_bin(self, hash_val):
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for (element,h) in bin:
                bin = self.get_bin(h)
                bin.append((element,h))
                self.used += 1

    def add(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        if (element,h) not in bin:
            bin.append((element,h))
            self.used += 1
            if self.used > self.size / 2:
                self.resize(int(2 * self.size))

    def remove(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        if (element,h) not in bin:
            raise ElementNotInSet()
        bin.remove((element,h))
        self.used -= 1
        if self.used < self.size / 4:
            self.resize(int(self.size / 2))

    def __iter__(self):
        for bin in self.array:
            yield from (element for (element,h) in bin)

    def __contains__(self, element):
        h = hash(element)
        bin = self.get_bin(h)
        return (element,h) in bin

    def __repr__(self):
        return 'HashTableSet(' + repr(list(iter(self))) + ')'

    def __len__(self):
        return self.used

x = HashTableSet([1, 2, 3, 5, 5, 7])
print(x)
print(len(x))
