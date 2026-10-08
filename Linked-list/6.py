#deleting the node in the linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Creation of linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:  # If list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:   # Traverse till last node
                temp = temp.next
            temp.next = new_node  # Append new node at the end

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_node(self, value):
        temp = self.head
        prev = None

        # Case 1: If head node itself holds the value
        if temp is not None and temp.data == value:
            self.head = temp.next  # Move head to next node
            temp = None            # Free the old head
            return

        # Case 2: Search for the node to delete
        while temp is not None and temp.data != value:
            prev = temp            # Store previous node
            temp = temp.next       # Move to next node

        # If value not found
        if temp is None:
            print("Value not found in the list")
            return

        # Case 3: Node found → unlink it
        prev.next = temp.next
        temp = None  # Free the node

# Example usage
list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

print("Original List:")
list.print()

list.delete_node(30)  # Delete node with value 30
print("After deleting 30:")
list.print()

list.delete_node(10)  # Delete head node
print("After deleting 10:")
list.print()

list.delete_node(100) # Try deleting non-existent node
