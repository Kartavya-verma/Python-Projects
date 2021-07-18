li = []
for i in range(int(input()) + 1):
    c = 0
    while i > 0:
        c += 1
        i = i & (i-1)
    li.append(c)
print(li)