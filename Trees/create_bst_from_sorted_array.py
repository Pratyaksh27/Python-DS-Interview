# Given a Sorted Array, create a balanced BST 

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def create_BST_from_sorted_array(list, start, end):
    if not list or start > end :
        return None
    if (start == end):
        return Node(list[start])
    mid = (start+end)//2
    # / is a float division
    # // is an int division
    root = Node(list[mid])
    root.left = create_BST_from_sorted_array(list, start, mid-1)
    root.right = create_BST_from_sorted_array(list, mid+1, end)
    return root

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)  # 👈 go deeper into right side first
        print('   ' * level + '->', node.value)  # 🖨️ indent & print
        print_tree(node.left, level + 1)  # 👈 then go into left side



list = [1,2,3,4,5,6,7,8]
root = create_BST_from_sorted_array(list, 0, len(list)-1)
# print_tree(root)
    