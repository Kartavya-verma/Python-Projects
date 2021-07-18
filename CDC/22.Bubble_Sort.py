def bubble(l):
    n = len(l)
    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swap = True
        if swap == False:
            break
    return l


l = list(map(int,input()))
print(bubble(l))