# li = [1, 1, 0, 1, 1, 1]
li = [1, 0, 1, 1, 0, 1]
c = 0
res = 0
for i in li:
    if i == 1:
        c += 1
    else:
        res = max(res, c)
        c = 0
print(max(c, res))