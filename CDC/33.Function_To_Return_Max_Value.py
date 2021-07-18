def maximum(l):
    temp = l[0]
    for i in range(1,len(l)):
        if l[i] > temp:
            temp = l[i]
    return temp


l = list(map(int,input().split()))
print(maximum(l))