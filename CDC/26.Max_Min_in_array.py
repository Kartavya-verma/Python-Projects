def min_max(l):
    mini = l[0]
    maxi = l[0]
    for i in range(1,len(l)):
        if mini > l[i]:
            mini = l[i]
    for i in range(1,len(l)):
        if maxi < l[i]:
            maxi = l[i]
    return(mini,maxi)


l = list(map(int,input().split()))
print(min_max(l))