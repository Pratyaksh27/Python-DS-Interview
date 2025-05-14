from generate_random_binary_trees import generate_random_binary_tree, print_tree_structure, print_tree_preorder
from create_bst_from_sorted_array import create_BST_from_sorted_array

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
root = create_BST_from_sorted_array(my_list, 0, len(my_list)-1)

def validate_bst(root):
    if not root:
        return True
    elif (not root.left and not root.right):
        return True
    elif not root.left:
        return (root.value < root.right.value and validate_bst(root.right))
    elif not root.right:
        return (root.value > root.left.value and validate_bst(root.left))
    return (root.value > root.left.value and root.value < root.right.value and validate_bst(root.left) and validate_bst(root.right))

# root = generate_random_binary_tree()
print_tree_structure(root)
if validate_bst(root):
    print(" Tree is a valid BST")
else:
    print("Tree is NOT a valid BST")