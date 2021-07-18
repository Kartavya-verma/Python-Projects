def onehop(lst):
    data = lst
    data.sort(key=lambda tup: tup[0])
    ans = []
    for ele in lst:
        x, y = ele
        for ele1 in lst:
            if ele != ele1:
                xx, yy = ele1
                if y == xx and x != yy and (x,yy) not in ans:
                    ans.append((x, yy))
    ans = sorted(ans, key=lambda tup: (tup[0], tup[1]))
    return ans