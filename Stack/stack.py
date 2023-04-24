class Stack:
    def __init_(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s = Stack()

while True:
    