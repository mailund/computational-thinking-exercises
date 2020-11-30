class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.prev = previous
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = DoublyLink(None, None, None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        return self.head.next == self.head

    def enqueue(self, x):
        # Put the new link at the end of the queue, i.e.
        # just before head
        link = DoublyLink(x, self.head.prev, self.head)
        link.prev.next = link ; link.next.prev = link

    def front(self):
        return self.head.next.element

    def dequeue(self):
        # Remove the front link and return its value
        val = self.head.next.element
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def print_queue(self):
        link = self.head.next
        while link != self.head:
            print(link.element)
            link = link.next

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()
print(queue.front())
queue.dequeue()
queue.print_queue()
