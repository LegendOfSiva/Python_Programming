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
        print(root.value, end=" \n")
        self.inorder_traversal(root.right)

    def contains_node(self, value):
        if not self.root:
            return
        current = self.root
        while current:
            if value == current.value:
                return f"\nNode {value} is found !!"
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return f"\nNode {value} is not found "

    def BFS(self, root):
        if not root:
            return "\nTree is empty "
        queue = [root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(result)


BST = binary_search_tree()
root = BST.insert_node(3)
BST.insert_node(5)
BST.insert_node(1)
BST.insert_node(8)

print("Inorder Traversal:")
BST.inorder_traversal(root)
BST.BFS(root)
print(BST.contains_node(8))
