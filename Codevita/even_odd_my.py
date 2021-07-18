from itertools import product

l, h = map(int, input().split())
k = int(input())
li = []
c = 0
mod = 1000000007
k = k % mod
l = l % mod
h = h % mod
for i in range(l, h + 1):
    li.append(i)
# print(li)
perm = product(li, repeat=k)
for i in perm:
    s = 0
    for j in range(len(i)):
        s = s + i[j]
    if s % 2 == 0:
        c += 1 % mod
print(c % mod)