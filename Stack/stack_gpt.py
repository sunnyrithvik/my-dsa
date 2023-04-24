class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())  # Output: 3
print(stack.peek())  # Output: 3
stack.pop()
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False
stack.pop()
stack.pop()
print(stack.is_empty())  # Output: True
