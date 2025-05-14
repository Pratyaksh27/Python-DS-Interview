


nums = [1,4,3,0,-1]

def merge_sort(nums, start, end):
    if start >= end:
        return nums
    mid = (start+end)//2
    # print(" ** Start ", start)
    # print("** End ", end)
    # print("** Mid ", mid)
    left_start = start
    left_end = mid
    right_start = mid+1
    right_end = end
    return merge(merge_sort(nums, left_start, left_end), merge_sort(nums,right_start,right_end), left_start, left_end, right_start, right_end)


def merge(left_list, right_list, left_start, left_end, right_start, right_end):
    ret_list = []
    if left_start > left_end:
        for i in range(right_start, right_end+1):
            ret_list.append(right_list[i])
        return ret_list
    if right_start > right_end:
        for i in range(left_start, left_end+1):
            ret_list.append(left_list[i])
        return ret_list
    if (left_list[left_start] <= right_list[right_start]):
        ret_list.append(left_list[left_start])
        return merge(left_list, right_list, left_start+1, left_end, right_start, right_end)
    else:
        ret_list.append(right_list[right_start])
        return merge(left_list, right_list, left_start, left_end, right_start+1, right_end)


merge_sort(nums, 0 , len(nums)-1)








