class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Delete a node from the list
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == data:
                    prev.next = current.next
                    break
            if current.next == self.head:
                prev.next = self.head

    # Print the list
    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print("\n")


LL = CircularLinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(5)
LL.print_list()
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.print_list()
LL.delete(20)
LL.print_list()
