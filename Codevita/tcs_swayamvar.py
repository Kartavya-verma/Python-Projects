n = int(input())
t = list(input())
r = list(input())
f = 0
for i in t[0:]:
    for j in r:
        if i in r:
            if i == j:
                t.remove(i)
                r.remove(j)
                break
        else:
            f = 1
            break
    if f == 1:
        break
print(len(t))


