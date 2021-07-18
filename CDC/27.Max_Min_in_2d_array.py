def min_max(l):
    a = l[0]
    for i in range(1,len(l)):
        a.extend(l[i])
    mini = a[0]
    maxi = a[0]
    for i in range(1, len(a)):
        if mini > a[i]:
            mini = a[i]
    for i in range(1, len(a)):
        if maxi < a[i]:
            maxi = a[i]
    return(mini,maxi)

l = [[1,2,3],[4,5,6],[7,8,9]]
print(min_max(l))