def majority(l):
    count = 0
    ele = 0
    for i in range(len(l)):
        if count == 0:
            ele = l[i]
        if ele == l[i]:
            count += 1
        else:
            count -= 1
    c = 0
    for i in range(len(l)):
        if l[i] == ele:
            c += 1
    if c > len(l) // 2:
        return ele
    else:
        return -1


l = list(map(int,input().split()))
print(majority(l))