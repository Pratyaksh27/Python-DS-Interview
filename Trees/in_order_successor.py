from generate_random_binary_trees import generate_random_binary_tree, print_tree_structure, print_tree_preorder
from create_bst_from_sorted_array import create_BST_from_sorted_array


# In Order Traversal in BST produces elements in sorted order
# How to find successor:
# If node.right, then find the smallest(leftmost) element in the node.right subtree
# Else Find an ancestor whose left subtree has the node. Keep going left till the value > node's value

# Assumption: Input Node WILL be in the Tree
# All elements are unique

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
root = create_BST_from_sorted_array(my_list, 0, len(my_list)-1)

'''
Aim: Find the smallest value that is GT node.value
1.) Set successor as None
2.) Continue to move root to right if root.value LT node.value. Else move left
3.) whenever we find that root's value is GT than node's value, we make that as the successor
'''

def in_order_successor(root, val):
    successor = None
    while root:
        if root.value > val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

'''
Aim: Find the Biggest element lesser than the node.value
1.) Set Predecessor as None
2.) Continue to move the root left if root.value GT than node.value. Else Move right
3.) Whenever the root.value is LT node.value, set it as predecessor
'''
def in_order_predecessor(root,val):
    predecessor = None
    while root:
        if root.value < val:
            predecessor = root
            root = root.right
        else:
            root = root.left
    return predecessor

val = 12
node = in_order_predecessor(root,val)
if node:
    print(" Predecessor is ", node.value)
else:
    print ("None")

    
    

        
    

    