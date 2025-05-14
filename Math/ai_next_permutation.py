def next_permutation(nums):
    # Step 1: Find the first decreasing element from the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # Step 2: If we found such an element, find the element just larger than it
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap them
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 3: Reverse the suffix in place
    start, end = i + 1, len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def next_perm(nums):
    if len(nums)==0 or len(nums)==1:
        return
    i = len(nums)-2
    while i>=0 and nums[i] > nums[i+1]:
        i-=1
    if i>=0:
        j = len(nums)-1
        while nums[j] < nums[i]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i] # Swap
    # Reverse from position i+1 to end
    start = i+1
    end = len(nums)-1
    while end >= start:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1
    return
    


# Testing the function with given test cases
test_cases = [
    [1, 2, 3, 4],
    [1, 4, 3, 2],
    [4, 3, 2, 1],
    [2, 1, 3, 4, 5],
    [1, 5, 2, 3, 4],
    [6, 1, 5, 4, 3, 2],
    [6, 5, 4, 3, 2, 1],
    [0, 6, 5, 4, 3, 2, 1],
    [10, 2, 9, 11, 7, 6, 5]
]

for case in test_cases:
    nums = case[:]
    next_perm(nums)
    print(f"Next permutation of {case} -> {nums}")