l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if(i==l[j]):
            l[i]=l[j]
            
print(l)

