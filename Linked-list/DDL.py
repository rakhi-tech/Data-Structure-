class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        temp=self.head  
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else: #First node
            self.head=new_node 
    def insert(self,new_node,pos) :
        
        if pos==1:
          new_node.next=self.head
          if self.head:
              
            self.head.prev=new_node
          
        else:
            temp = self.head
            p=1
            while temp and p < pos-1:
                temp = temp.next
                p+=1
            if temp is None:
                print("Position out of range:")
                return
            new_node.next = temp.next
            if temp.next:
                temp.next.prev=new_node
            temp.next = new_node
            new_node.prev= temp

    def print(self):
        temp=self.head
        print("List Emements: ")
        while temp:
            print(temp.data, " ")  
            temp=temp.next 

list1=LinkedList()
list1.append(Node(12))                         
list1.append(Node(52))                         
list1.append(Node(51))                         
list1.append(Node(102))                         
list1.append(Node(16)) 
list1.print()
list1.insert(Node(5),1) 
list1.print()

