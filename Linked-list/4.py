#inserting the node at different position in linked list
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
#creation of linked list
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if (self.head==None):
            self.head = new_node
        else: 
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node #appending the node
    def insert(self,new_node,pos):
        temp=self.head
        if pos == 7: #inserting at first position
            
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            while(p!= pos-1 or temp.next!=None):
                temp = temp.next
                
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            return
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.insert(Node(100),1)
list.print()
list.insert(Node(66),7)
list.print

           