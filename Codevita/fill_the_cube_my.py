from math import floor
n = int(input())
l = []
for i in range(n):
    l.append(list(map(str, input().split())))

l2 = [row.count('C') for row in l]
s = sum(l2)
print(floor(s ** 0.5) + 1)


# for j in range(len(l)):
#     for k in range(len(l)):
#         if l[j][k] == 'D':
#             c += 1
# print(c)
# print(floor(c**0.5))