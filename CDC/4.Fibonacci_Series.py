n = int(input())
if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    z = 0
    f = 1
    print(z,f,end=" ")
    for i in range(2,n):
        s = z + f
        print(s, end=" ")
        z = f
        f = s