def smallest(l):
    res = 1
    for i in range(len(l)):
        if l[i] <= res:
            res += l[i]
        else:
            break
    return res


l = list(map(int, input().split()))
print(smallest(l))