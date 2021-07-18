t=int(input())
d=[i for i in range(1,101)]
for i in range(t):
    M,x,y=map(int,input().split())
    dist=list(map(int,input().split()))
    temp=[]
    for j in dist:
        if(j-x*y-1<0):
            temp+=d[0:j+x*y]
        else:
            temp+=d[j-x*y-1:j+x*y]
    print(len(list(set(d)-set(temp))))