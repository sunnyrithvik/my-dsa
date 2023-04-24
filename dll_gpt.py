class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, current.next)
            current = current.next
        print("*********************")


LL = DoublyLinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(5)
LL.display()
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.display()
LL.delete(20)
LL.display()
