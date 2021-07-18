x = int(input())
l = []
for i in input().split():
    l += [int(i)]
l=set(l)

y = int(input())
l1 = []
for i in input().split():
    l1 += [int(i)]
l1=set(l1)
l3=list(sorted(l.union(l1)-l.intersection(l1)))
for i in l3:
    print(i)