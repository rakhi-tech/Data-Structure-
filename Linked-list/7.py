#Reversing the linked list
# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.next = None      # Pointer to the next node

# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None      # Initially the list is empty

    # Append a new node at the end
    def append(self, new_node):
        if self.head is None:   # If list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:    # Traverse till last node
                temp = temp.next
            temp.next = new_node

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
 
    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # Store next node
            current.next = prev        # Reverse the link
            prev
    # Create linked list
ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

print("Original List:")
ll.print_list()

# Reverse the list
ll.reverse()
print("Reversed List:")
ll.print_list()