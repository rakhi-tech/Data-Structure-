# Doubly Linked List 
# Doubly Linked List Implementation with Reverse Print

# Node class represents each element in the DLL
class Node:
    def __init__(self, value):
        self.prev = None   # Pointer to the previous node
        self.data = value  # Data stored in the node
        self.next = None   # Pointer to the next node

# LinkedList class manages the whole DLL
class LinkedList:
    def __init__(self):
        self.head = None   # Start of the list

    # Append a node at the end
    def append(self, new_node):
        if self.head is None:        # If list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:         # Traverse till last node
                temp = temp.next
            temp.next = new_node     # Link last node to new node
            new_node.prev = temp     # Link new node back to last node

    # Print all elements in forward order
    def print_forward(self):
        temp = self.head
        print("Forward Order: ", end="")
        while temp:
            print(temp.data, end=" ")
            last = temp              # Keep track of last node
            temp = temp.next
        print()
        return last                  # Return last node for reverse traversal

    # Print all elements in reverse order
    def print_reverse(self):
        # First go to the last node
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        # Now traverse backwards using prev pointers
        print("Reverse Order: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

# ------------------ Testing ------------------

list1 = LinkedList()

# Append nodes
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(51))
list1.append(Node(102))
list1.append(Node(16))

# Print in forward order
list1.print_forward()   # Output: 12 52 51 102 16

# Print in reverse order
list1.print_reverse()   # Output: 16 102 51 52 12
