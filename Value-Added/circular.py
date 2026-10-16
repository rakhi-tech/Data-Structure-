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

    # Display list
    def display(self):
        nodes = []
        temp = self.head
        if not self.head:
            print("List is empty")
            return
        while True:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes), "-> (back to head)")

