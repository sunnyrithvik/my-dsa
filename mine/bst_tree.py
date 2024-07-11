class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            self.data = data
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, val):
        if val == self.data:
            return str(val) + " is found in the list"
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return str(val) + " is not found in the list"
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return str(val) + " is not found in the list"

    def getmin(self):
        temp = self
        while temp.left != None:
            temp = temp.left
        return temp.data

    def getmax(self):
        temp = self
        while temp.right != None:
            temp = temp.right
        return temp.data

    def inorder(self):
        if self.left:
            print(self.left.inorder())
        print(self.data)
        if self.right:
            print(self.right.inorder())

    def preorder(self):
        print(self.data)
        if self.left:
            print(self.left.preorder())
        if self.right:
            print(self.right.preorder())

    def postorder(self):
        if self.left:
            print(self.left.postorder())
        if self.right:
            print(self.right.postorder())
        print(self.data)

    def delete(self, val):
        if self.data is None:
            return
        if val < self.data:
            self.left = self.left.delete(val)
        if val > self.data:
            self.right = self.right.delete(val)

        if val == self.data:
            if self.left == None and self.right == None:
                return self

            if self.left == None:
                return self.right

            if self.right == None:
                return self.left

            if self.left != None and self.right != None:
                pass


root = Node(15)
root.insert(19)
root.insert(17)
root.insert(11)
root.insert(13)
root.insert(21)
root.insert(9)
root.PrintTree()
print(root.search(19))
print(root.getmin())
print(root.getmax())
