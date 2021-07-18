t=int(input())
for i in range(t):
    n=int(input())
    c=1
    for j in range(n,1,-1):
        c=c*j
    print(c)