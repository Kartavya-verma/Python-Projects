def selection(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] >l[j]:
                l[i],l[j] = l[j],l[i]
    return l


l = list(map(int,input().split()))
print(selection(l))