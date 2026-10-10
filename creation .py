class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp.next = new_node
    def print(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next()

ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))
ll.append(Node(50))
ll.print()