def getSum(no):
    return 0 if no == 0 else int(no%10) + getSum(int(no/10))

for i in range(int(input())):
    c = 0
    m = 0
    for j in range(int(input())):
        a,b=map(int,input().split())
        aout=getSum(a)
        bout=getSum(b)
        if(aout<bout):
           m=m+1
        elif(aout>bout):
            c=c+1
        else:
            c=c+1
            m=m+1
    if(c>m):
        print("0 "+str(c))
    elif(c<m):
        print("1 "+str(m))
    else:
        print("2 "+str(c))