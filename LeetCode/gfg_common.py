res = []
v1 = {1, 5, 10, 20, 40, 80}
v2 = {6, 7, 20, 80, 100}
v3 = {3, 4, 15, 20, 30, 70, 80, 120}
for i in v1:
   if i in v2 and i in v3:
       res.append(i)
res.sort()
print(res)