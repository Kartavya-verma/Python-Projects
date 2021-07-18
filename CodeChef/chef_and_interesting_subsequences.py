# 30% correct but Time Limit Exceeded   //Without video / Self
# def sequences(arr, index, subarr):
#     if index == len(arr):
#         if len(subarr) != 0:
#             if len(subarr) == k:
#                 li.append(sum(subarr))
#     else:
#         sequences(arr, index + 1, subarr)
#         sequences(arr, index + 1, subarr + [arr[index]])
#     return
#
#
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     li = []
#     sequences(arr, 0, [])
#     print(li.count(min(li)))



# Method - 1 Correct       // With reference to video

# from math import gcd
#
#
# def nCr(n, r):
#     p = 1
#     z = 1
#     if n - r < r:
#         r = n - r
#     if r != 0:
#         while r:
#             p *= n
#             z *= r
#             m = gcd(p, z)
#             p //= m
#             z //= m
#             n -= 1
#             r -= 1
#     else:
#         p = 1
#     return p
#
#
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     last = arr[k - 1]
#     c = 0
#     for i in range(n):
#         if arr[i] == last:
#             c += 1
#     num = 0
#     for i in range(k):
#         if arr[i] == last:
#             num += 1
#     print(nCr(c, num))




# Method - 2 Correct (Modification of Mehtod - 1)

# def nCr(n, r):
#     return int(fact(n) / (fact(r) * fact(n - r)))
#
#
# def fact(n):
#     res = 1
#     for j in range(2, n + 1):
#         res = res * j
#
#     return res
#
#
# for _ in range(int(input())):
#     x, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     last = arr[k - 1]
#     c = 0
#     for i in range(x):
#         if arr[i] == last:
#             c += 1
#     num = 0
#     for i in range(k):
#         if arr[i] == last:
#             num += 1
#     print(nCr(c, num))




# Method - 3 Correct (Optimal & Simplified)

from math import factorial

for i in range(int(input())):
    x, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    fac = factorial
    # print(arr)
    n = arr.count(arr[k - 1])     # Count of 2 = 3
    # print(c, arr[k-1])
    r = arr[:k].count(arr[k - 1])
    # print(r, arr[:k])
    print(int(fac(n) / (fac(n - r) * fac(r))))  # nCr = n! / (n-r)! * r!