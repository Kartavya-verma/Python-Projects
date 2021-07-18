l = [1,1]
i = 0
while i < len(l):
    if l[i] != l[l[i] - 1]:
        temp = l[l[i] - 1]
        l[l[i] - 1] = l[i]
        l[i] = temp
    else:
        i += 1
print(l)
res = []
for i in range(len(l)):
    if l[i] != i+1:
        res.append(l[i])
        res.append(i+1)
        l[i] = i+1
print(res)
print(l)