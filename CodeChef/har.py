l1=list(map(int,input().split()))
s=set(l1)
l3=list(s)
l2=l3[:]
l4=[]
for i in range(len(s)):
    count=0
    for j in range(len(l1)):
        if(l3[i]==l1[j]):
            count+=1
    l4.append(count)
flag=0
flag2=0
for i in range(len(l4)):
    if l4[i]==1:
        flag+=1
        pos=i
if(flag==1):
    l3.remove(l3[pos])
    if(l3==sorted(l3)):
        for i in range(len(l1)):
            if(l1[i]==l2[pos]):
                if(i==0 or i==len(l1)-1):
                    print("Yes")
                elif(l1[i-1]!=l1[i+1]):
                    print("Yes")
                else:
                    print("No")
    else:
        print("No")
else:
    print("No")