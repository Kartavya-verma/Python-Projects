def plus(l):
    ind = len(l) - 1
    while ind >= 0:
        if l[ind] < 9:
            l[ind] += 1
            return l
        else:
            l[ind] = 0
        ind -= 1
    l.insert(0,1)
    return l


l = list(map(int,input().split()))
print(plus(l))