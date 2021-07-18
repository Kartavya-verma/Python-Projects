# # row = 100000000
# letters = input()
# t = input()
# q = int(input())
# # l = letters * row
#
# for _ in range(q):
#     n = int(input())
#     l = letters * n
#     for i in range(1, n + 1):
#         p = l[0:i]
#         if i == n:
#             if t in p:
#                 print(p.count(t))
#             else:
#                 print(0)

import math
letters = input()
t = input()
q = int(input())
for _ in range(q):
    n = int(input())
    print(math.floor(n/len(t)))