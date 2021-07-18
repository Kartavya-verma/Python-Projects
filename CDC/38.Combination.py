# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         f = 1
#         for i in range(2, a + 1):
#             f *= i
#         return f
#
#
# n = int(input())
# r = int(input())
# res = fact(n) // (fact(r) * fact(n-r))
# print(res)

# def combination(n,r):
# #     if r > n:
# #         return 0
# #     if t[n][r] != -1:
# #         return t[n][r]
# #     elif r == 0 or r == n:
# #         t[n][r] = 1
# #         return t[n][r]
# #     else:
# #         t[n][r] = combination(n-1,r) + combination(n-1,r-1)
# #         return t[n][r]
# #
# #
# # n = int(input())
# # r = int(input())
# # t = [[-1 for y in range(r + 1)]for x in range(n + 1)]
# # print(combination(n,r))



def combination(n,r):
    t = [[0 for y in range(r + 1)] for x in range(n + 1)]
    m = 1000000007
    for i in range(n+1):
        for j in range(min(i,r)+1):
            if j == 0 or j == i:
                t[i][j] = 1
            else:
                t[i][j] = (t[i-1][j] + t[i-1][j-1]) % m
    return t[n][r]


n = int(input())
r = int(input())
print(combination(n,r))


# def binomialCoeff(n, k):
#     C = [0 for i in range(k + 1)]
#     C[0] = 1
#     for i in range(1, n + 1):
#         j = min(i, k)
#         while j > 0:
#             C[j] = C[j] + C[j - 1]
#             j -= 1
#     return C[k]
#
#
# n = int(input())
# k = int(input())
# print(binomialCoeff(n, k))