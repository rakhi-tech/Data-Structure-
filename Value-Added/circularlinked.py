class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head   # circular link
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insert at beginning
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Delete a node by value
    def delete(self, key):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if prev:  # not head
                    prev.next = current.next
                else:     # deleting head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    # Display list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# 🎮 Test Circular Linked List
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()

cll.prepend(5)
cll.display()

cll.delete(20)
cll.display()



