class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right


def inorder(temp):
    if temp is None:
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def level_order(rt):
    if rt is None:
        print("BST is empty")
        return

    arr = []
    cnt = 0
    level=0
    arr.append(rt)

    while cnt < len(arr):
        node_count=len(arr)-cnt#no of nodes to be visited 
        print("\n level:",level,end = "")
        for i in range(node_count):
         temp = arr[cnt]
         cnt += 1

         print(temp.data, end="   ")

         if temp.left:
            arr.append(temp.left)

         if temp.right:
            arr.append(temp.right)
        level+=1


# Main Program
t = BST()

t.insert(Node(10))
t.insert(Node(18))
t.insert(Node(20))
t.insert(Node(33))
t.insert(Node(37))
t.insert(Node(76))

print("Inorder Traversal:")
inorder(t.root)

print("\nLevel Order:")
level_order(t.root)