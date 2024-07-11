class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data)
        if self.head != None:
            node.link = self.head
            self.head = node
        else:
            self.head = node
        print("Inserted element " + str(data) + " at the beginning")

    def insert_at_end(self, data):
        node = Node(data)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = node
        else:
            self.head = node
        print("Inserted element " + str(data) + " at the end")

    def delete_node(self, ele):
        if self.head == None:
            print("List is Empty")
            return
        if self.head.data == ele:
            temp = self.head
            self.head = temp.link
            temp = None
            return
        current = self.head
        while current.link != None:
            if current.link.data == ele:
                temp = current.link
                current.link = temp.link
                temp = None
                print("Deleted Element " + str(ele))
                return
            current = current.link
        print("Element is not found in the List")

    def search(self, ele):
        if self.head == None:
            print("list is empty")
            return
        current = self.head
        while current != None:
            if current.data == ele:
                print("Element " + str(ele) + " found in the list")
                return
            current = current.link
        print("Element " + str(ele) + " is not found in the List")

    def display(self):
        print("----------")
        print("List:")
        if self.head == None:
            print("List Empty")
            return
        current = self.head
        while current != None:
            print(current.data)
            current = current.link
        print("----------")


LL = LinkedList()
LL.insert_at_begin(3)
LL.insert_at_begin(7)
LL.insert_at_begin(9)
LL.display()
LL.insert_at_end(10)
LL.insert_at_end(13)
LL.display()
LL.delete_node(13)
LL.delete_node(3)
LL.display()
LL.search(7)
LL.search(17)
