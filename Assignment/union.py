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
print(len(l.symmetric_difference(l1)))
