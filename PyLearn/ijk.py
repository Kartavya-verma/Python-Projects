l=list(map(int,input().split()))
l1=l
for i in range(len(l)):
    for j in range(len(l)):
        if(i!=l[j]):
            l1[i]=-1
        else:
            l1[i]=l[j]
print(l1)