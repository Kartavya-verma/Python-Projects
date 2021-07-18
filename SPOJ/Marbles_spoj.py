# from math import factorial
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     n -= 1
#     k -= 1
#     print(factorial(n) // (factorial(n-k)*factorial(k)))


# def c(n1, k1):
#     ans = 1
#     if k1 > n1 - k1:
#         k1 = n1 - k1
#     for i in range(1, k1+1):
#         ans *= (n1 - i + 1)
#         ans //= i
#     return ans
#
#
# t = int(input())
# while t:
#     n, k = map(int, input().split())
#     print(c(n-1, k-1))
#     t -= 1

