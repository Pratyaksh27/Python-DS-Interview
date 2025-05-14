from create_bst_from_sorted_array import create_BST_from_sorted_array

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
start = create_BST_from_sorted_array(my_list, 0, len(my_list)-1)

def create_list_of_lists_by_level(root):
    list_of_lists = []
    if not root:
        return
    first_list = [root]
    list_of_lists.append(first_list)

    while True:
        current_list = list_of_lists[-1]
        next_list = []
        for node in current_list:
            if node.left:
                next_list.append(node.left)
            if node.right:
                next_list.append(node.right)
        if next_list:
            list_of_lists.append(next_list)
        else:
            break
    
    return list_of_lists

def print_lists_by_level(list_of_lists):
    for i in range (0, len(list_of_lists)):
        print(" Level ", i)
        for node in list_of_lists[i]:
            print(node.value, " -- ")

lists_by_level = create_list_of_lists_by_level(start)
print_lists_by_level(lists_by_level)

