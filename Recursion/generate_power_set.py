nums = [1,2,3]
# Op is [[], [1], [2], [3], [1,2],[1,3], [2,3], [1,2,3]]
# PS[1,2,3] = PS[1] + PS[2] +PS[3] +PS[1,2]...

def generate_power_set(nums, start, end):
    if start == end:
        return [[], [nums[start]]]
    recursive_power_set = generate_power_set(nums, start, end-1)
    return_power_set = []
    for subset in recursive_power_set:
        new_subset = [x for x in subset]
        new_subset.append(nums[end])
        return_power_set.append(subset)
        return_power_set.append(new_subset)
    return return_power_set


ret = generate_power_set(nums, 0 , len(nums)-1)
print(ret)
    

    
