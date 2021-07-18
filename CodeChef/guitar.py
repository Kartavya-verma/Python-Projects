for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    sum=0
    for k in range(len(li)-1):
        if(li[k]<li[k+1]):
            sum+=((li[k+1]-li[k])-1)
        elif(li[k]>li[k+1]):
            sum+=((li[k]-li[k+1])-1)
        else:
            sum+=0
    print(sum)