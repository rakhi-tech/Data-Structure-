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
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
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

    arr = [rt]
    cnt = 0
    level = 0

    while cnt < len(arr):

        node_count = len(arr) - cnt

        print(f"\nLevel {level} :", end=" ")

        for i in range(node_count):
            temp = arr[cnt]
            cnt += 1

            print(temp.data, end=" ")

            if temp.left:
                arr.append(temp.left)

            if temp.right:
                arr.append(temp.right)

        level += 1


# Main Program
t = BST()

t.insert(Node(50))
t.insert(Node(30))
t.insert(Node(70))
t.insert(Node(20))
t.insert(Node(40))
t.insert(Node(60))
t.insert(Node(80))

print("Inorder Traversal:")
inorder(t.root)

print("\n\nLevel Order Traversal:")
level_order(t.root)