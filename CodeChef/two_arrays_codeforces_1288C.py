from math import factorial
mod = 10**9 + 7
n, m = map(int, input().split())
print(factorial(n + 2*m - 1) // (factorial(2*m) * factorial(n - 1)) % mod)