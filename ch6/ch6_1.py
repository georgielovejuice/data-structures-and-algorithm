count1, count2 = 0,0
def fibo(n):
    global count1
    count1 += 1

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibo(n - 1) + fibo(n - 2))

def fibo_m(n, memo=None):
    """Fibonacci with memoization"""
    global count2
    memo = {} if memo is None else memo

    if n in memo:
        return memo[n]
    count2 += 1

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibo_m(n - 1, memo) + fibo_m(n - 2, memo)
    return memo[n]
    

print(" *** Find fibonacci sequence ***")
n = int(input('Enter n : '))
print(f"fibo({n}) = {fibo(n)} count = {count1:,}")
print(f"fibo_m({n}) = {fibo_m(n)} count = {count2}")
print("===== End of program =====")