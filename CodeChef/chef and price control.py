t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    l1=[y if i>y else i for i in l]
    s1=sum(l1)
    print(s-s1)

