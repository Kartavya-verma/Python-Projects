def countsqu(f):
    cnt = 0
    for i in range(0, f + 1):
        j = 1;
        while j * j <= i:
            if j * j == i:
                # print(i)
                cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt

p = int(input())
q = int(input())
r = int(input())
s = int(input())
t = 0
for i in range(p,q+1):
    for j in range(r,s+1):
        f = i*j
        c = countsqu(f)
        t = t + c
print(t)



        # print(f,"x",f)
        # d=i*j-f*f
        # print(d)