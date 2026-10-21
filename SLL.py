class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Append (create linked list)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Traverse and print
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert at specific position (1-based index)
    def insert_at(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete alternate nodes
    def delete_alternate(self):
        temp = self.head
        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original List:")
ll.traverse()

ll.insert_at(3, 25)
print("After inserting 25 at position 3:")
ll.traverse()

ll.delete_alternate()
print("After deleting alternate nodes:")
ll.traverse()
