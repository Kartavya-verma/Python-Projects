li = []
res = []
while(True):
    i = input()
    if i == 'q':
        break
    elif i != '42.195':
        li.append(float(i))
for i in range(3):
    res.append(max(li))
    li.remove(max(li))
print(res)