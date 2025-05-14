import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_random_binary_tree(depth=4, min_val=-50, max_val=50, prob_branch=0.7):
    """Generate a random binary tree up to a certain depth."""
    def build(current_depth):
        if current_depth == 0 or random.random() > prob_branch:
            return None
        node = TreeNode(random.randint(min_val, max_val))
        node.left = build(current_depth - 1)
        node.right = build(current_depth - 1)
        return node
    
    root = TreeNode(random.randint(min_val, max_val))  # always make a root
    root.left = build(depth - 1)
    root.right = build(depth - 1)
    return root


def print_tree_preorder(node):
    """Simple preorder print of the tree"""
    if node:
        print(node.value, end=' ')
        print_tree_preorder(node.left)
        print_tree_preorder(node.right)

def print_tree_structure(node, level=0):
    if node is not None:
        print_tree_structure(node.right, level + 1)
        print('   ' * level + '->', node.value)
        print_tree_structure(node.left, level + 1)


tree = generate_random_binary_tree()
# print("Preorder Traversal:")
# print_tree_preorder(tree)
# print("------------")
# print_tree_structure(tree, 0)