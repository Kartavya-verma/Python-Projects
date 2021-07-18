# for _ in range(int(input())):
#     h, p = map(int, input().split())
#     li = []
#     for i in range(p):
#         h = h - p
#         p = p//2
#         if p <= 0 < h:
#             li.append(0)
#             break
#         elif h <= 0 < p:
#             li.append(1)
#             break
#     for j in li:
#         print(j)

# for _ in range(int(input())):
#     h, p = map(int, input().split())
#     for i in range(p):
#         h = h - p
#         p = p // 2
#         # print(h, p)
#         if p <= 0 < h:
#             print(0)
#             break
#         elif h < p:
#             print(1)
#             break

for _ in range(int(input())):
    h, p = map(int, input().split())
    while p > 0:
        h = h - p
        p = p // 2
    if h > 0:
        print(0)
    else:
        print(1)













