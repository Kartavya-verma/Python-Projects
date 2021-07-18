def pos_neg(l):
    pos = []
    neg = []
    res = []
    for i in l:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    print(pos, neg)
    for i in range(len(neg)):
        pos.insert(i + (i + 1), neg[i])
    return(pos)


l = list(map(int,input().split()))
print(pos_neg(l))



# for i in tuple(zip(pos,neg)):
#     res.append(i[0])
#     res.append(i[1])
# print(res)