l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if(i==l[j]):
            temp=l[i]
            l[i] = l[j]
            l[j]=temp
            c=c+1
    #if(c==0):
      # l[i]=-1
    #print(l[i])
for i in range(len(l)):
    print(l[i],end=" ")
