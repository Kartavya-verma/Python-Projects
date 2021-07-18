def funutil(d,sset,n):
    m=99999999
    for i in range(n+1):
        if d[i]<m and sset[i]==False:
            m=d[i]
            res=i
    return res

def fun(g,s,f,n):
    d=[99999999 for _ in range(n+1)]
    d[s]=0
    sset=[False for _ in range(n+1)]
    for _ in range(n+1):
        u=funutil(d,sset,n)
        sset[u]=True
        for i in range(n+1):
            if g[u][i]>0 and sset[i]==False and d[i]>d[u]+g[u][i]:
                d[i]=d[u]+g[u][i]
    return d[f]

idmap={}
n=int(input())
for i in range(n):
    x=int(input())
    idmap[x]=i+1
m=int(input())
g=[[999999 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,input().split())
    x=idmap[x]
    y=idmap[y]
    g[x][y]=z
s=idmap[int(input())]
f=idmap[int(input())]
print(fun(g,s,f,n))