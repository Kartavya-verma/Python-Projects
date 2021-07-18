n = int(input())
s = set(map(int, input().split()))
m= int(input())
for i in range(m):
    name,*line=input().split()
    l=list(map(int,line))
    if(name=='pop'):
        s.pop()
    elif(name=='remove'):
        s.remove(l[0])
    elif(name=='discard'):
        s.discard(l[0])
print(sum(s))