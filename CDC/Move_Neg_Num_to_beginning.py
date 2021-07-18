l = [-12,11,-13,-5,6,-7,5,-3,-6]
j = 0
for i in range(len(l)):
    if l[i] < 0:
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        j += 1
print(l)



# l = list(map(int,input().split()))
# s = 0
# e = len(l)-1
# while s <= e:
#     if l[s] > l[e]:
#         l[s],l[e] = l[e],l[s]
#         s += 1
#         e -= 1
#     elif l[s] < l[e]:
#         s += 1
#     else:
#         e -= 1
# print(l)