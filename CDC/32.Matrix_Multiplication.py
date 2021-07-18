# n = int(input())
# m = int(input())
# l = []
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(int(input()))
#     l.append(a)
# print(l)
#
# l1 = []
# for i in range(n):
#     a1 = []
#     for j in range(m):
#         a1.append(int(input()))
#     l1.append(a1)
# print(l1)

x = [[1,7,3,],[3,5,6],[6,8,9]]
y = [[1,1,1,2],[6,7,3,0],[4,5,9,1]]
# res = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# for i in range(len(x)):
#     for j in range(len(y[0])):
#         for k in range(len(y)):
#             res[i][j] += x[i][k] * y[k][j]

res = [[sum(a*b for a,b in zip(a_row,b_col)) for b_col in zip(*y) for a_row in x]]
print(res)