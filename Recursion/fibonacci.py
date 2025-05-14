
def fibonacci(n):
    if n < 0:
        return None
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def fibonacci_memo(n, memo={}):
    if n < 0:
        return None
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


n=5
print(fibonacci_memo(5))
    