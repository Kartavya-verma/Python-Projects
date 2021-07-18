def sumprimes(l):
    sum=0
    count=0

    for i in range(0,len(l)):
        flag=1
        if(l[i]==2):
            sum=sum+2
        elif(l[i]<=1):
            count=count+l[i]
        else:
            for j in range(2,l[i]):
                if(l[i]%j==0):
                    flag=0
            if(flag==1):
                sum=sum+l[i]
    print(sum)
    return 0


sumprimes([17,51,29,39])
sumprimes([-3,-5,3,5])
sumprimes([4,6,15,27])

