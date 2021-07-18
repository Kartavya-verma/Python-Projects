n = 2
arr = [2, 2]
l = []
for i in arr:
    if i not in l:
        l.append(i)
    else:
        print("Repeating number is",i)

for i in range(1, len(arr) + 1):
    if i not in l:
        print("Missing Number is", i)

d = {}
res = []
for i in arr:
    if i not in d:
        d[i] = True
    else:
        res.append(i)
for i in range(1, len(arr) + 1):
    if i not in d:
        res.append(i)