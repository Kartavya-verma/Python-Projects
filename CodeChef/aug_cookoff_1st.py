# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     li = list(map(int, input().split()))
#     c = 0
#     # s = 0
#     if n > 1:
#         for i in range(len(li)):
#             s = 0
#             if li[i] > k:
#                 print(-1)
#                 break
#             else:
#                 if i != n - 1:
#                     s += li[i]
#                     if s + li[i+1] <= k:
#                         c += 1
#                         i += 2
#                     else:
#                         c += 1
#
#         print(c)
#     else:
#         if li[0] > k:
#             print(-1)
#         else:
#             print(1)



# t = int(input())
# while t != 0:
#     n, k = map(int, input().split())
#     w = list(map(int, input().split()))
#     c = 1
#     s = 0
#     for i in w:
#         if i > k:
#             c = -1
#             break
#         else:
#             s += i
#             # w.remove(i)
#             if s > k:
#                 # print(s)
#                 c += 1
#                 s = 0
#             if len(w) == 1:
#                 c = +1
#     print(c)
#
#     t -= 1

for _ in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    c = 0
    f = 0
    for i in range(len(li)):
        s = li[i]
        if li[i] > k:
            f = 1
            break
        else:
            while s <= k:
                s += li[i + 1]
                i += 1
        if s > k:
            i -= 1
        c += 1
    if f == 0:
        print(c)
    else:
        print(-1)