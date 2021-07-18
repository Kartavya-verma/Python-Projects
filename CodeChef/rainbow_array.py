# for i in range(int(input())):
#     n = int(input())
#     li = list(map(int, input().split()))
#     if max(li) == 7:
#         if len(li) % 2 != 0:
#             l1 = li[:n // 2]
#             l2 = li[n // 2 + 1:]
#             l2.sort()
#         # print(l1, l2)
#         else:
#             l1 = li[:n // 2 - 1]
#             l2 = li[n // 2:]
#             l2.sort()
#         # print(l1, l2)
#         if l1 == l2:
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("no")

for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    s = {1, 2, 3, 4, 5, 6, 7}
    if max(li) == 7 and s == set(li) and li == li[::-1]:
        print("yes")
    else:
        print("no")