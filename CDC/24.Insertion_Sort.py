def insertion(l):
    for i in range(1,len(l)):
        current_ele = l[i]
        pos = i
        while current_ele < l[pos-1] and pos>0:
            l[pos] = l[pos-1]
            pos -= 1
        l[pos] = current_ele
    return l

l = list(map(int,input().split()))
print(insertion(l))