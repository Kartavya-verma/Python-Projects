# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     li = list(map(int, input().split()))
#     res = {}
#     for i in li:
#         if k % i == 0:
#             res[i] = k//i
#     if len(res) == 0:
#         print(-1)
#     else:
#         print(res[min(res.values())])


for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    res = []
    for i in p:
        if k % i == 0:
            res.append(i)
    if len(res) == 0:
        print(-1)
    else:
        print(max(res))
