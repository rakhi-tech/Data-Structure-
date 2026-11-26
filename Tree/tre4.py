class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Find deepest node
    def get_deepest_node(self):
        if self.root is None:
            return None

        queue = [self.root]
        while queue:
            temp = queue.pop(0)

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        return temp

    # Delete deepest node
    def delete_deepest(self, d_node):
        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp == d_node:
                temp = None
                return

            if temp.left:
                if temp.left == d_node:
                    temp.left = None
                    return
                queue.append(temp.left)

            if temp.right:
                if temp.right == d_node:
                    temp.right = None
                    return
                queue.append(temp.right)

    # Delete a node
    def delete(self, key):
        if self.root is None:
            return

        if self.root.left is None and self.root.right is None:
            if self.root.data == key:
                self.root = None
            return

        queue = [self.root]
        key_node = None

        while queue:
            temp = queue.pop(0)

            if temp.data == key:
                key_node = temp

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        if key_node:
            deepest = self.get_deepest_node()
            key_node.data = deepest.data
            self.delete_deepest(deepest)


# Driver Code
bt = BinaryTree()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Inorder before deletion:")
bt.inorder(bt.root)

bt.delete(20)

print("\nInorder after deletion:")
bt.inorder(bt.root)