class Node:
    def __init__(self, val):
        self.data = val
        self.next = None   # इथे error fix

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def delete_middle(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next   # middle delete

# Example usage
ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))
ll.append(Node(50))

print("Original List:")
ll.print_list()

middle = ll.find_middle()
print("Middle node value:", middle.data)

ll.delete_middle()
print("After deleting middle node:")
ll.print_list()
