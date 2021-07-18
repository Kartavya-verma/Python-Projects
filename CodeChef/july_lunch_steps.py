# for i in range(int(input())):
#     n, k = map(int, input().split())
#     c = ""
#     while n > 0:
#         d = int(input())
#         if d % k == 0:
#             c += "1"
#         else:
#             c += "0"
#         n -= 1
#     print(c)

for i in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int,input().split()))
    c = ""
    for j in d:
        if j % k == 0:
            c += "1"
        else:
            c += "0"
    print(c)