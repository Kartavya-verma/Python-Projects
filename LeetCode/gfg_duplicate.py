n = 11
a = [10,10,7,7,7,4,0,5,10,5,10]
res = []
# for i in list(set(a)):
#     if a.count(i) > 1:
#         res.append(i)
# print(*res)
a.sort()
for i in range(n-1):
    if a[i] == a[i+1]:
        res.append(a[i])
        i += 1
res = sorted(list(set(res)))
print(res)