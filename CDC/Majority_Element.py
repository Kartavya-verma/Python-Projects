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
    return ele

l = [3,1,3,3,2]
print(majority(l))