def merge_sort(nums, start, end):
    if start == end:
        return [nums[start]]

    mid = (start + end) // 2
    left = merge_sort(nums, start, mid)
    right = merge_sort(nums, mid + 1, end)
    return merge(left, right)

def merge(left, right):
    result = []
    print(" Beginning List is :", result)
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    print(" Ending List is :", result)
    return result

# Usage
nums = [1, 4, 3, 0, -1]
ret_list = merge_sort(nums, 0, len(nums) - 1)
print("Sorted:", ret_list)
