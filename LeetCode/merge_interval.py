# interval = [[1,3],[2,6],[8,10],[15,18]]
interval = [[1,4],[4,5]]
n = interval.copy()
print(n)
res = []
v = []
for i in range(len(n)-1):
    for j in range(len(n)):
        print(n[i][1], n[i+1][0])
        if n[i][1] > n[i+1][0]:
            # print(n[i][1], n[i+1][0])
            n[i].pop()
            n[i].append(n[i+1][1])
            v = n[i+1]
            print(n[i],v)
n.remove(v)
print(n)


# l = list()
# for i in interval:
#     for j in range(i[0], i[1]+1):
#         l.append(j)
# print(l)