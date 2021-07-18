def jump(l):
    reach = 0
    for i in range(len(l)):
        if i > reach:
            return 0
        reach = max(reach,i+l[i])
    return 1


l = list(map(int,input()))
print(jump(l))