#stack implementation using linked list
class noode:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("poped element:",temp.data)
            self.top=self.top.next
            temp=None
    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("stack contains..")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next


st=Stack() 
st.push(noode(20))
st.push(noode(40))
st.push(noode(50))
st.push(noode(60))
st.print()
st.pop()
st.print()



