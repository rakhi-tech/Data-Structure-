class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed")

    def pop(self):
        if not self.is_empty():
            print(self.stack.pop(), "popped")
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
print("hello rakhi")