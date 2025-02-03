data = 100

def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

def rev(n):
    ans = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        ans = ans * 10 + digit
    return ans
