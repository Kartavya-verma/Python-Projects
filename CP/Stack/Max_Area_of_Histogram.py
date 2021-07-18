l = [6,2,5,4,5,1,6]
# op = [1,5,3,5,5,7,7]
st =[]
res = []
pseudo_ind = 7
for i in range(len(l)-1,-1,-1):
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
    st.append([l[i],i])
res.reverse()
# print(res)

# op = [-1,-1,1,1,3,-1,5]
st1 =[]
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
    st1.append([l[i],i])
# print(res1)

wid = []
for i in range(len(l)):
    wid.append(res[i]-res1[i]-1)
# print(wid)
area = []
for i in range(len(l)):
    area.append(wid[i] * l[i])
print(max(area))