class Node:
    def __init__(self, info, prev=None, next=None):
        self.info = info
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, ele):
        node = Node(ele)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_end(self, ele):
        node = Node(ele)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current

    def delete_node(self, ele):
        # base case
        if self.head == None:
            print("List is Empty")
            return

        # if only one node is present
        if self.head.next == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp = None
                return
            else:
                print("Element is not found in our list")
                return

        # delete node in between
        temp = self.head.next
        while temp.next != None:
            if temp.info == ele:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return

        # delete last node
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        print("Element is not found in the list")

    def display(self):
        if self.head == None:
            print("List is Empty")
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.next
        print("****************")


LL = LinkedList()
LL.insert_at_begin(10)
LL.insert_at_begin(5)
LL.display()
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.display()
LL.delete_node(20)
LL.display()
