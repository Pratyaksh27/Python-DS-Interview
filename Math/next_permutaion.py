'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''

def calculate_next_permutation(list_num):
    print("Input is ", list_num)
    for i in range(0,len(list_num)):
        if is_all_descending(list_num, i):
            if i==0:
                print(list_num.reverse())
                return 
            swap(list_num,i-1,len(list_num)-1)
            reverse_nums(list_num,i)
    print("Output is ", list_num)
    return

def is_all_descending(list_num, start_pos):
    # print("In IS ALL DESecnding Start position: ", start_pos, " Starting Element is ", list_num[start_pos])
    if start_pos == len(list_num)-1:
        return True
    for i in range(start_pos,len(list_num)-1):
        if list_num[i] < list_num[i+1]:
            return False
    return True

def reverse_nums(list_num, start_pos):
    # print("Reverese Nums Start Pos ", start_pos)
    for i in range(0,len(list_num)):
        if len(list_num)-1-i > start_pos+i:
            swap(list_num, start_pos+i, len(list_num)-1-i)
    return

def swap(list_num, pos_a, pos_b):
    # print("SWAP Start and End Positions :", pos_a, " ", pos_b)
    c = list_num[pos_a]
    list_num[pos_a] = list_num[pos_b]
    list_num[pos_b] = c
    return


list_num1 = [1,2,3,4]
list_num2 = [1,4,3,2]
list_num3 = [2,1,3,4,5]
list_num4 = [4,3,2,1]
list_num5 = [1,5,2,3,4]
list_num6 = [6,1,5,4,3,2]
list_num7 = [6,5,4,3,2,1]
list_num8 = [0,6,5,4,3,2,1]
calculate_next_permutation(list_num1)
calculate_next_permutation(list_num2)
calculate_next_permutation(list_num3)
calculate_next_permutation(list_num4)
calculate_next_permutation(list_num5)
calculate_next_permutation(list_num6)
calculate_next_permutation(list_num7)
calculate_next_permutation(list_num8)
'''
Test Cases
[1,2,3,4] = [1,2,4,3]
[1,4,3,2] = [2,1,3,4]
[4,3,2,1] = [1,2,3,4]
[2,1,3,4,5] = [2,1,3,5,4]
[1,5,2,3,4] = [1,5,2,4,3]
[6,1,5,4,3,2] = [6,2,1,3,4,5]
[6,5,4,3,2,1] = [1,2,3,4,5,6]
[0,6,5,4,3,2,1] = [1,0,2,3,4,5,6]
'''