# def subset(l,s,n):
#     t = [[False for x in range(s+1)] for i in range(n+1)]
#     for i in range(n+1):
#         for j in range(s+1):
#             if j == 0:
#                 t[i][j] = True
#     for i in range(1,n+1):
#         for j in range(1,s+1):
#             if l[i-1] > j:
#                 t[i][j] = t[i-1][j]
#             elif l[i-1] <= j:
#                 t[i][j] = t[i-1][j-l[i-1]] + t[i-1][j]
#     return t[n][s]
#


# def subset(l,s,n,c):
#     for i in range(n):
#         for j in range(i+1,n):
#             if l[i] + l[j] == s:
#                 c += 1
#     return c


# Python 3 implementation of simple method
# to find count of pairs with given sum.
import sys

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def subset(l,n,s):
    t = [0] * 10000000
    for i in range(n):
        t[l[i]] += 1
    count = 0
    for i in range(n):
        count += t[s-l[i]]
        if s - l[i] == l[i]:
            count -= 1
    return count//2


nm = int(input())
s = int(input())
l = list(map(int,input().split()))
n = len(l)
print(subset(l,n,s))