class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Leaf nodes have height 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def insert_node(node, val):
            if not node:
                return AVLNode(val)

            if val < node.val:
                node.left = insert_node(node.left, val)
            elif val > node.val:
                node.right = insert_node(node.right, val)
            else:
                return node  # no duplicates

            # Update height
            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))

            # Check balance
            balance = self.get_balance(node)

            # Balancing cases
            if balance > 1 and val < node.left.val:
                return self.rotate_right(node)

            if balance < -1 and val > node.right.val:
                return self.rotate_left(node)

            if balance > 1 and val > node.left.val:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            if balance < -1 and val < node.right.val:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = insert_node(self.root, val)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1, prefix="R---- ")
        print("     " * level + prefix + str(node.val))
        if node.left:
            self.print_tree(node.left, level + 1, prefix="L---- ")


if __name__ == "__main__":
    tree = AVLTree()
    for val in [1, 5, 10, 15, 25, 24]:
        print(f"\nInserting {val}:")
        tree.insert(val)
        tree.print_tree()
