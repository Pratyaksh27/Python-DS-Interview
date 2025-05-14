'''
Aim of Min Heap (PQ): Allow fast access O(1) to minimum element
and O(log) to Insertion and Deletion
Its Kept as a List(array) and Visualized as a tree

        0
      /   \
     1     5                =  [0, 1, 5, 3, 4, 7, 8, 6]
    / \   / \
   3  4  7   8
  /
 6

1.) Parent element is Smaller than each Child
2.) Complete Binary Tree => Each level is filled before the next level starts filling
3.) Element at index i has childern at indices 2i+1 and 2i+2. And Parent at (i-1)//2 (integer division (floor))
4.) Insertion: Add at the end of the array. If Heap Property is broken, bubble it up by swapping
5.) Deletion: Replace first element of array with Last element. If Heap prop is broken, bubble it down
'''

class Priority_Queue:
    def __init__(self):
        self.list = []
    
    def append(self, value):
        PQ = self.list
        PQ.append(value)
        child_index = len(PQ)-1
        parent_index = (child_index - 1)//2
        while child_index > 0 and PQ[parent_index] > PQ[child_index]:
            PQ[parent_index], PQ[child_index] = PQ[child_index], PQ[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1)//2
    
    
    def delete(self):
        PQ = self.list
        if not PQ:
            return None
        min_ele = PQ[0]
        PQ[0] = PQ.pop()
        PQ_len = len(PQ)
        parent_index = 0
        child1_index, child2_index = 2*parent_index+1, 2*parent_index+2
        smallest_index = parent_index
        while child1_index < PQ_len or child2_index < PQ_len:
            if child1_index < PQ_len and PQ[smallest_index] > PQ[child1_index]:
                smallest_index = child1_index
            if child2_index < PQ_len and PQ[smallest_index] > PQ[child2_index]:
                smallest_index = child2_index
            if smallest_index == parent_index:
                break 
            PQ[smallest_index], PQ[parent_index] = PQ[parent_index], PQ[smallest_index]
            parent_index = smallest_index
            child1_index, child2_index = 2*parent_index+1, 2*parent_index+2
        return min_ele
    
    def print_pq(self):
        for i in self.list:
            print(i,"  ", end = " ")
        print()
            


Que = Priority_Queue()
Que.append(10)
Que.print_pq()
Que.append(9)
Que.print_pq()
Que.append(1)
Que.print_pq()
Que.append(4)
Que.print_pq()

Que.delete()
Que.print_pq()
Que.delete()
Que.print_pq()
Que.delete()
Que.print_pq()

