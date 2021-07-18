l = list(map(int,input().split(",")))
dic = {}
res = []
t = []
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] < l[j]:
            if l[j] not in dic.keys():
                dic[l[j]] = l[i+1:].count(l[j])
    if len(dic) != 0:
        # print(dic)
        s = max(dic.values())
        for x in dic:
            if dic[x] == s:
                res.append(x)
        t.append(min(res))
    else:
        t.append(-1)
    dic.clear()
    res.clear()
for y in range(len(t)):
    if y != len(t)-1:
        print(t[y],end=",")
    else:
        print(t[y])










        # l = list(map(int, input().split(",")))
        # dic = {}
        # res = []
        # t = []
        # for i in range(len(l)):
        #     for j in range(i + 1, len(l)):
        #         if l[i] < l[j]:
        #             if l[j] not in dic.keys():
        #                 dic[l[j]] = l[i + 1:].count(l[j])
        #     if len(dic) != 0:
        #         # print(dic)
        #         s = max(dic.values())
        #         for x in dic:
        #             if dic[x] == s:
        #                 res.append(x)
        #         t.append(min(res))
        #         dic.clear()
        #         res.clear()
        #     else:
        #         t.append(-1)
        #         dic.clear()
        #         res.clear()
        # print(t)