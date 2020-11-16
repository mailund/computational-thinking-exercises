class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.previous = previous
        self.next = next

def insert_list_after(link, begin, end):
    end.next = link.next
    end.next.previous = end
    begin.previous = link
    link.next = begin

def insert_after(link, element):
    new_link = DoublyLink(element, None, None)
    insert_list_after(link, new_link, new_link)

def remove_link(link):
    link.previous.next = link.next
    link.next.previous = link.previous

class DoublyLinkedListSequence(object):
    def __init__(self):
        # make a dummy head and point it at itself
        self.dummy = DoublyLink(None, None, None)
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy

    def append(self, element):
        insert_after(self.dummy.previous, element)

    def prepend(self, element):
        insert_after(self.dummy, element)

    def get_at_index(self, index):
        return self.get_link(index).element

    def set_at_index(self, index, value):
        self.get_link(index).element = value

    def extend(self, other):
        insert_list_after(self.dummy.previous,
                          other.dummy.next,
                          other.dummy.previous)

    def insert_sequence_at(self, index, other):
        link = self.get_link(index)
        insert_list_after(link,
                          other.dummy.next,
                          other.dummy.previous)

    def remove_first(self):
        if self.dummy.next == self.dummy:
            raise IndexError("Empty sequence")
        remove_link(self.dummy.next)

    def remove_last(self):
        if self.dummy.next == self.dummy:
            raise IndexError("Empty sequence")
        remove_link(self.dummy.previous)

    def remove_first(self):
        if self.dummy.next == self.dummy:
            raise IndexError("Empty sequence")
        remove_link(self.dummy.next)

    def remove_last(self):
        if self.dummy.next == self.dummy:
            raise IndexError("Empty sequence")
        remove_link(self.dummy.previous)

    def __str__(self):
        links = []
        link = self.dummy.next
        while link != self.dummy:
            links.append("[{}]".format(link.element))
            link = link.next
        return "->".join(links)

dllist = DoublyLinkedListSequence()
for i in range(10):
    dllist.append(i)
print(dllist)
