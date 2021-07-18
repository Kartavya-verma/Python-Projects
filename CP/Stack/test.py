def mah(l):
    # op = [1,5,3,5,5,7,7]
    st = []
    res = []
    pseudo_ind = len(l)
    for i in range(len(l) - 1, -1, -1):
        if len(st) == 0:
            res.append(pseudo_ind)
        elif len(st) > 0 and st[-1][0] < l[i]:
            res.append(st[-1][1])
        elif len(st) > 0 and st[-1][0] >= l[i]:
            while len(st) > 0 and st[-1][0] >= l[i]:
                st.pop()
            if len(st) > 0 and st[-1][0] < l[i]:
                res.append(st[-1][1])
            else:
                res.append(pseudo_ind)
        st.append([l[i], i])
    res.reverse()
    # print(res)

    # op = [-1,-1,1,1,3,-1,5]
    st1 = []
    res1 = []
    pseudo_ind1 = -1
    for i in range(len(l)):
        if len(st1) == 0:
            res1.append(pseudo_ind1)
        elif len(st1) > 0 and st1[-1][0] < l[i]:
            res1.append(st1[-1][1])
        elif len(st1) > 0 and st1[-1][0] >= l[i]:
            while len(st1) > 0 and st1[-1][0] >= l[i]:
                st1.pop()
            if len(st1) > 0 and st1[-1][0] < l[i]:
                res1.append(st1[-1][1])
            else:
                res1.append(pseudo_ind1)
        st1.append([l[i], i])
    # print(res1)

    wid = []
    for i in range(len(l)):
        wid.append(res[i] - res1[i] - 1)
    # print(wid)
    area = []
    for i in range(len(l)):
        area.append(wid[i] * l[i])
    return(max(area))


l2 = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
n = len(l2)
m = len(l2[0])
v = []
for j in range(m):
    v.append(l2[0][j])
mx = mah(v)
# print(mx)
for i in range(1,n):
    for j in range(m):
        if l2[i][j] == 0:
            v[j] = 0
        else:
            v[j] = v[j] + l2[i][j]
    mx = max(mx, mah(v))
print(mx)