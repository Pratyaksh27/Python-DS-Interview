'''
Complete Tree  = The Next Level Starts filling up only when the current level is fully filled. 
And Every Level is filled from left to right ONLY

    A
  /  \       = Complete
B     C 

    A
  /         = Complete
B

    A
      \     = Not Complete
        C

        A
      /   \
    B       D  = Not Complete
   /       /
C         E  
'''
from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

def validate_complete_tree(root: Node):
    if not root:
        return True
    que = deque()
    que.append(root)
    is_none_encountered = False
    while que:
        node = que.popleft()
        if node is not None:
            if is_none_encountered:
                return False
            que.append(node.left)
            que.append(node.right)
        else:
            is_none_encountered = True
    return True


