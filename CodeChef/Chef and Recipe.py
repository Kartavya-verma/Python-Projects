for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=0;flag=1
    done=[];done1=[]
    while(i<n):
        if a[i] in done:
            print("NO")
            flag=0
            break
        else:
            c= a[i]
            done.append(c)
            count=0
            while(i<n and a[i]==c):
                i+=1
                count+=1
            if count in done1:
                print("NO")
                flag=0
                break
            else:
                done1.append(count)
    if flag :
        print("YES")