from itertools import product

def sum_of(n):
    s = 0
    for i in range(len(n)):
        s = s + int(n[i])
    return s


l, h = map(int, input().split())
k = int(input())
li = []
for i in range(l, h + 1):
    li.append(str(i))
co = 0
p = 10 * 9 + 7
perm = product(li, repeat=k)
for i in perm:
    # print(sum_of(i))
    if sum_of(i) % 2 == 0:
        co += 1
print(co % p)