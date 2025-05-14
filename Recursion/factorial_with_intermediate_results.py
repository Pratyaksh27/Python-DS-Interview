'''
Input: A positive integer
Output: List of all intermediate results
Ex. Input = 5
Output = [1, 2, 6, 24, 120] 
'''

def factorial_with_intermediate_results(n):
    if n==0 or n==1:
        return ([1])
    else:
        ret_list = factorial_with_intermediate_results(n-1)
        last_val = n * ret_list[-1]
        ret_list.append(last_val)
        return ret_list
    
n = 6
ret = factorial_with_intermediate_results(n)
print(ret)