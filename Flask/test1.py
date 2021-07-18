t=int(input())
for i in range(t):
    x = [int(x) for x in input().split()]
    ar= list([int(x) for x in input().split()])

    li=[]
    for i in range(x[1],0,-1):
        li.append(i)

    # ind=[index for index, value in enumerate(ar) if value == x[1]]
    # print(ind)

    # for q in range(ar.index(x[1])):
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


