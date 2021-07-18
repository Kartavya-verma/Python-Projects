l = [100, 80, 60, 70, 60, 75, 85]
# op = [1, 1, 1, 2, 1, 4, 6]
st = []
res = []
for i in range(len(l)):
    if len(st) == 0:
       res.append(-1)
    elif len(st) > 0 and st[-1][0] > l[i]:
        res.append(st[-1][1])
    elif len(st) > 0 and st[-1][0] <= l[i]:
        while len(st) > 0 and st[-1][0] <= l[i]:
            st.pop()
        if len(st) == 0:
            res.append(-1)
        else:
            res.append(st[-1][1])
    st.append([l[i], i])
# print(res)
for i in range(len(l)):
    res[i] = i - res[i]
print(res)