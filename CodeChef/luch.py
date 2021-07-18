for i in range(int(input())):
    s,n=input().split()
    s=int(s)
    n=int(n)
    if(s%n==0):
        print(s//n)
    elif(s==1):
        print(1)
    else:
        temp=0
        n1=s
        while(n>0):
            temp=n1//n
            n1=n1%n
            if(n1<n):
                n=n//2
                temp = n1 // n
                n1 = n1 % n