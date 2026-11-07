class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, item):
        self.stack.append(item)

    # Pop element
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Size of stack
    def size(self):
        return len(self.stack)

    # Display stack
    def display(self):
        print(self.stack)



s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()         
print(s.peek())      
print(s.pop())       
s.display()          
print(s.size())   