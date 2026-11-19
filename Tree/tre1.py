#Binary search Tree
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