class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            self.size -= 1
            return popped_node.data

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def is_empty(self):
        return self.top == None

    def get_size(self):
        return self.size


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_size())  # Output: 3
print(stack.peek())  # Output: 3
stack.pop()
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False
stack.pop()
stack.pop()
print(stack.is_empty())  # Output: True
