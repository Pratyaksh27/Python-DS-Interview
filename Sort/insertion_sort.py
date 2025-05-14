'''
🔸 “Find the correct index where the current value belongs,
🔸 shift everything to the right to make space,
🔸 and write that value into that position.”
'''

def insertion_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return 
    for i in range(1,len(nums)):
        inserted_val = nums[i]
        j = i
        while j>=1:
            if nums[j-1] > inserted_val:
                nums[j] = nums[j-1]
            else:
                nums[j] = inserted_val
                break
            j -=1
            if (j == 0):
                nums[j] = inserted_val
    return


nums = [5,3,4,2,1,99]
# nums = [5,3,4,2,1]
# nums = [1,2,3,4,5]
# nums = [5]
# nums = []
insertion_sort(nums)
print(nums)




















