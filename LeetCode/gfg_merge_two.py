l1 = [1, 3, 5, 7]
l2 = [0, 2, 6, 8, 9]
n = len(l1)
m = len(l2)
l3 = l1.copy()
l4 = l2.copy()
l1.clear()
l2.clear()
l3.extend(l4)
l3.sort()
print(l1,l2,l3)
for i in range(n):
    l1.append(l3[i])
for i in range(m):
    l2.append(l3[i+n])
print(l1,l2)