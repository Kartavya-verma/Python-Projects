l = [1, 3, 2, 4]
# op = [3, 4, 4, -1]
st = []
res = []
for i in range(len(l) - 1, -1, -1):
    if len(st) == 0:
       res.append(-1)
    elif len(st) > 0 and st[-1] > l[i]:
        res.append(st[-1])
    elif len(st) > 0 and st[-1] <= l[i]:
        while len(st) > 0 and st[-1] <= l[i]:
            st.pop()
        if len(st) == 0:
            res.append(-1)
        else:
            res.append(st[-1])
    st.append(l[i])
print(res)
res.reverse()
print(res)