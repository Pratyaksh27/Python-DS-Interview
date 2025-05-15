'''
Write a function to determine if two binary trees are exactly the same — meaning both the structure and node values match.
'''

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


def check_if_2_trees_are_identical(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 and root2:
        return False
    elif root1 and not root2:
        return False
    elif root1.val != root2.val:
        return False
    else:
        return check_if_2_trees_are_identical(root1.left, root2.left) and check_if_2_trees_are_identical(root1.right, root2.right)