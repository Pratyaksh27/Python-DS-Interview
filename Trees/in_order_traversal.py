from generate_random_binary_trees import generate_random_binary_tree, print_tree_structure, print_tree_preorder
from create_bst_from_sorted_array import create_BST_from_sorted_array

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
root = create_BST_from_sorted_array(my_list, 0, len(my_list)-1)

print_tree_structure(root)

def in_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    print(" ", root.value)
    in_order_traversal(root.right)

in_order_traversal(root)