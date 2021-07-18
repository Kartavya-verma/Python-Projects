l = [4,5,2,10,8]
# op = [3,4,4,1]
st =[]
res = []
for i in range(len(l)):
    if len(st) == 0:
        res.append(-1)
    elif len(st) > 0 and st[-1] < l[i]:
        res.append(st[-1])
    elif len(st) > 0 and st[-1] >= l[i]:
        while len(st) > 0 and st[-1] >= l[i]:
            st.pop()
        if len(st) > 0 and st[-1] < l[i]:
            res.append(st[-1])
        else:
            res.append(-1)
    st.append(l[i])
# res.reverse()
print(res)