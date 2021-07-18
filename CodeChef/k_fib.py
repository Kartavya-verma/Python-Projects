# n, k = map(int,input().split())
# l = []
# for i in range(k):
#     l.append(1)
# # print(l)
# sum = 0
# for j in range(len(l)):
#     sum = sum + l[j]
#     if(j == len(l)-1):
#         # print("Outer",sum)
#         l.insert(0, sum)
#         print(l)
#         for p in range(k-1):
#             sum = sum + l[p+1]
#         # l.insert(0, sum)
#         print(sum)

n, k = map(int,input().split())
l = []
for i in range(k):
    l.append(1)
# print(l)
sum = 0
item = 1
for j in l[:k]:
    if n>len(l):
        sum = sum + j
    print(sum)
    l.insert(0, sum)
            # print(l)