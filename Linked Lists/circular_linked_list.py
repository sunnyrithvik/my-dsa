class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, ele):
        node = Node(ele)
        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            current = self.head
            while current.head != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.head = node

    def insert_at_end(self, ele):
        node = Node(ele)
        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def delete_node(self, ele):
        if self.head == None:
            print("List is Empty")
            return
        if self.head.info == ele:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next.info == ele:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next
        print("Element is not found in the list")

    def display(self):
        current = self.head
        while current.next != self.head:
            print(current.info)
            current = current.next
        print(current.info)


ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.display()
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
ll.delete_node(20)
ll.display()
