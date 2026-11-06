
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data

    def reverse(self):
        temp_stack = stack()

        while not self.isempty():
            temp_stack.push(Node(self.pop()))

        self.top = temp_stack.top
        temp_stack.top = None

    def reverse_string(self, string):
        for ch in string:
            self.push(Node(ch))

        rev = ""

        while not self.isempty():
            rev += self.pop()

        return rev

    def print(self):
        temp = self.top

        while temp:
            print(temp.data)
            temp = temp.next


st = stack()
st1 = stack()
st2 = stack()

st1.push(Node(10))
st1.push(Node(40))
st1.push(Node(60))
st1.push(Node(50))
st1.push(Node(25))

print("original stack:")
st1.print()

st1.pop()

print("after pop:")
st1.print()

st1.reverse()

print("after reverse:")
st1.print()

string = "hello DSA"

print("Original String:", string)
print("Reversed String:", st.reverse_string(string))