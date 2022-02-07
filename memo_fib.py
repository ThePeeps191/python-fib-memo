memo = {}
def fib(n, memo):
    if n in memo.keys():
        return memo[n]
    if n in [1, 2]:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result
