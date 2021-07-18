t=int(input())
for i in range(t):
    x = [int(x) for x in input().split()]
    ar= list([int(x) for x in input().split()])

    li=[]
    for i in range(x[1],0,-1):
        li.append(i)


    def removeElements(li,ar):
        for i in range(len(ar) - len(li) + 1):
            for j in range(len(li)):
                if ar[i + j] != li[j]:
                    break
            else:
                return True
        return False

    if(removeElements(li,ar)==True):
        temp=0
        temp=temp+1
    print(temp)


