'''
📜 Statement:
Given an array of integers (can include negatives and zeros), 
return the maximum product of any two distinct elements.

Input: [-10, -3, 1, 2]
Output: 30
Explanation: (-10) * (-3) = 30

Test Case
[-10, -3, 1, 2]
[-10]
[-10, -3]
[]
[0,0,0,0,1,0]
[-10, -3, 1, 2, -5]
[-10, -3, 1, -11, -5]
'''

def max_product_2_integers(nums):
    max_product = 0
    if len(nums) == 0 or len(nums) == 1:
        return max_product
    elif len(nums) == 2:
        return nums[0]*nums[1]
    for  i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            product = nums[i]*nums[j]
            if product > max_product:
                max_product = product
    return max_product

nums = [-1, -3, 1, -11, -5]
print(max_product_2_integers(nums)) 