#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
       
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def del_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
                rt.left= self.del_node(rt.left,val)
        elif val>rt.data:
                rt.right=self.del_node(rt.right,val)
        else:
         if rt.left is None:
            return rt.right
         if rt.right is None:
            return rt.left
         succ=self.get_successor(rt)
         rt.data=succ.data
         rt.right=self.del_node(rt.right,succ.data)
        return rt
    def get_succcessor(self,temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp
        
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)

    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
print("\nInorder: ")
b1.inorder(b1.root)
#print("\nNo of nodes: ",b1.cnt)
print("\nPreorder: ")
b1.preorder(b1.root)
print("\nPostorder: ")
b1.postorder(b1.root)
b1.findminmax()
b1.del_node(b1.root,2)
print("\n After deleting",end=" ")
b1.inorder(b1.root)