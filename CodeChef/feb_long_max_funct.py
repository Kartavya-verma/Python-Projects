# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     res = [abs(l[-1] - l[0])]
#     for i in range(len(l) - 1):
#         res.append(abs(l[i] - l[i+1]))
#         print(res)
#     print(sum(res))

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(2*(max(l) - min(l)))