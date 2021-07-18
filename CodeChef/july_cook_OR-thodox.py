# i = int(input())
# while i != 0:
#     n = int(input())
#     l = list(map(int, input().split()))
#     l1 = []
#     for j in range(len(l)):
#         for k in range(j+1):
#             l1.append(l[j] | l[k])
#     if len(l1) != len(set(l1)):
#         print("NO")
#     else:
#         print("YES")
#     i = i-1

# i = int(input())
# while i != 0:
#     n = int(input())
#     l = list(map(int, input().split()))
#     l1 = []
#     j = 0
#     while j != len(l):
#         k = 0
#         while k != j+1:
#             l1.append(l[j] | l[k])
#             k = k + 1
#         j = j + 1
#     if len(l1) != len(set(l1)):
#         print("NO")
#     else:
#         print("YES")
#     i = i-1


# for i in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     l1 = []
#     temp = l[0]
#     for j in range(1,len(l)):
#         temp |= l[j]
#         l1.append(temp)
#     if len(l1) != len(set(l1)):
#         print("NO")
#     else:
#         print("YES")

print(3 | 7)