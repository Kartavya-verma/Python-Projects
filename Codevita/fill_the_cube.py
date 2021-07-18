from math import floor
n = int(input())
l = []
c = 0
for i in range(n):
    l1 = list(map(str, input().split()))
    l.append(l1)
for j in range(n):
    for k in range(n):
        if l[j][k] == 'D':
            c += 1
print(floor(c ** 0.5))


