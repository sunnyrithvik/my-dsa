class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
