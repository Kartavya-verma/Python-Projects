for i in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    if(n==m):
        print(2*(n*(n-1)+m*(m-1)))