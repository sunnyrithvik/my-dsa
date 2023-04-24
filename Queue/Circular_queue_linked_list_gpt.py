class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return value

    def is_empty(self):
        return self.head is None
