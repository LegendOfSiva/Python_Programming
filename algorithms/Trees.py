class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class binary_search_tree:
    def __init__(self) -> None:
        self.root = None

    def insert_node(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new_node
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new_node
                        break
        return self.root

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.value, end=" ")
        self.inorder_traversal(root.right)


BST = binary_search_tree()
root = BST.insert_node(3)
BST.insert_node(5)
BST.insert_node(1)
BST.insert_node(8)

print("Inorder Traversal:")
BST.inorder_traversal(root)
