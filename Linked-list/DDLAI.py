

# Doubly Linked List Implementation in Python

# Node class represents each element in the list
class Node:
    def __init__(self, value):
        self.prev = None   # Pointer to the previous node
        self.data = value  # Data stored in the node
        self.next = None   # Pointer to the next node

# LinkedList class manages the whole list
class LinkedList:
    def __init__(self):
        self.head = None   # Start of the list

    # Append a node at the end of the list
    def append(self, new_node):
        if self.head is None:        # If list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:         # Traverse till last node
                temp = temp.next
            temp.next = new_node     # Link last node to new node
            new_node.prev = temp     # Link new node back to last node

    # Insert a node at a specific position
    def insert(self, new_node, pos):
        if pos == 1:                 # Insert at beginning
            new_node.next = self.head
            if self.head:            # If list is not empty
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            p = 1
            while temp and p < pos-1:  # Traverse to (pos-1)th node
                temp = temp.next
                p += 1
            if temp is None:
                print("Position out of range")
                return
            new_node.next = temp.next
            if temp.next:            # If not inserting at the end
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    # Print all elements in the list
    def print(self):
        temp = self.head
        print("List Elements: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# ------------------ Testing ------------------

list1 = LinkedList()

# Append nodes at the end
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(51))
list1.append(Node(102))
list1.append(Node(16))
list1.print()   # Output: 12 52 51 102 16

# Insert at beginning
list1.insert(Node(5), 1)
list1.print()   # Output: 5 12 52 51 102 16

# Insert at 3rd position
list1.insert(Node(99), 3)
list1.print()   # Output: 5 12 99 52 51 102 16
