n=int(input())
l=[]
for i in input().split():
    l+=[int(i)]
l=set(l)
m=int(input())
for i in range(m):
    l1=[]
    name,r=input().split()
    r=map(int,r)
    for j in input().split():
        l1+=[int(j)]
    l1=set(l1)
    if(name=='intersection_update'):
        l.intersection_update(l1)
    elif(name=='update'):
        l.update(l1)
    elif(name=='symmetric_difference_update'):
        l.symmetric_difference_update(l1)
    elif(name=='difference_update'):
        l.difference_update(l1)
print(sum(l))
