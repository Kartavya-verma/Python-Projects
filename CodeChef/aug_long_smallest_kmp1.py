# for _ in range(int(input())):
#     s = list(input())
#     p = list(input())
#     res = ""
#     for i in p:
#         s.remove(i)
#     s.sort()
#     co = s.copy()
#     print(co)
#     co.append(p[0])
#     print(co)
#     co = sorted(co, reverse=True)
#     print(co)
#     if p[0] not in s:
#         print("".join(s[0:len(co) - co.index(p[0])-1]) + "".join(p) + ''.join(s[len(co) - co.index(p[0])-1:]))
#     else:
#         air = ''.join(s[0:s.index(p[0])]) + ''.join(p) + ''.join(s[s.index(p[0]):])
#         print(min(air, "".join(s[0:len(co) - co.index(p[0]) - 1]) + "".join(p) + "".join(s[len(co) - co.index(p[0]) - 1:])))


for _ in range(int(input())):
    s = list("zaazyz")
    p = "azy"
    for x in p:
        s.remove(x)
    s = "".join(sorted(s))
    i = 0
    for x in p:
        print(x, p[0])     ## 1.a  a   2.z  a
        if x != p[0]:
            print(x, p[0])          ## Loop out    z   a
            if x < p[0]:
                i = 1
            break
    print(p[0], i)           ## p[0]=a   i=0
    if p[0] not in s:         ## p[0]=a   s= zaazyz
        s = "".join(sorted(s + p[0]))
        if i == 0:
            n = s.rindex(p[0])
        else:
            n = s.index(p[0])
        s = s[:n] + p + s[n + 1:]
    # print(s)                        #azz

    else:
        if i == 0:
            # print(s.rindex(p[1]))
            # print(s.index(p[1]))
            n = s.rindex(p[0])
        else:
            n = s.index(p[0])
        s = s[:n] + p + s[n:]
    print(s)
