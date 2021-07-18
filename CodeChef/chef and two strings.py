t=int(input())
for i in range(t):
    s1,s2=input(),input()
    m,n=0,0
    for i in range(len(s1)):
        if(s1[i]=='?' or s2[i]=='?' ):
            m+=1
        elif(s1[i]!=s2[i]):
            n+=1
    print(n,n+m)
