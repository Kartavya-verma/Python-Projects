# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     fa = list(map(int, input().split()))
#     fa.sort()
#     c = 0
#     for i in range(len(fa)):
#         if fa.count(fa[i]) > 1:
#             c = fa.count(fa[i])
#             if fa[i] != max(fa):
#                 c = c - 1
#     print(c + k)



# kartik
# t = int(input())
# while t != 0:
#     n, k = map(int, input().split())
#     fa = list(map(int, input().split()))
#     r = []
#     f1 = []
#     if len(set(fa)) == len(fa):
#         print(k)
#     else:
#         sp = k + len(fa) - len(set(fa)) + 1
#         for i in range(0, n):
#             if fa[i] != fa[i+1]:
#                 r.append(i , i+1)
#     t -= 1

# Harshala
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l1 = list(set(l))
    l2 = []
    for x in l1:
        l2.append(l.count(x))
    m = max(l1)
    l3 = []
    for i in range(len(l2)):
        if l2[i] > 1:
            if l1[i] != m:
                l2[i] -= 1
            l3.append(l2[i])
    result = k+sum(l3)
    print(result)