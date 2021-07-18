# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     i,j,count = 0,m-1,0
#     A.sort()
#     B.sort()
#     if sum(A) > sum(B):
#         print(0)
#     else:
#         while sum(A) < sum(B) and i < n and j > -1:
#             if A[i] != B[j]:
#                 print(A[i],B[i])
#                 A[i], B[j] = B[j], A[i]
#                 count += 1
#             i += 1
#             j -= 1
#         if sum(A) > sum(B):
#             print(count)
#         else:
#             print(-1)

# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     c = 0
#     sum_a = sum(A) % 10000
#     sum_b = sum(B) % 10000
#     if sum_a > sum_b:
#         print(0)
#     else:
#         while sum_a < sum_b:
#             min_a = A.index(min(A))
#             max_b = B.index(max(B))
#             temp = A[min_a]
#             A[min_a] = B[max_b]
#             B[max_b] = temp
#             sum_a = sum(A) % 10000
#             sum_b = sum(B) % 10000
#             c += 1
#         # print(A)
#         # print(B)
#         if sum(A) > sum(B):
#             print(c)
#         else:
#             print(-1)
#

# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     count = 0
#     for i in range(n):
#         if sum(A) > sum(B):
#             break
#         else:
#             A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]
#             count+=1
#     if sum(A) > sum(B):
#         print(count)
#     else:
#         print(-1)


for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    while n:
        if sum(a) > sum(b):
            break
        else:
            a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
            c += 1
        n -= 1
    if sum(a) > sum(b):
        print(c)
    else:
        print(-1)