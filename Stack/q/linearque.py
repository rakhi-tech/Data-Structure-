class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class lQ:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        print("deleted node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("queue is empty now")
            self.rear=None
        temp=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
que=lQ()
que.enqueue(node(23))
que.enqueue(node(24))
que.enqueue(node(25))
que.enqueue(node(26))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()
