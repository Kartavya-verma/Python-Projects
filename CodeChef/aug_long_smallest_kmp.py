# for _ in range(int(input())):
#     s = list(input())
#     p = input()
#     res = ""
#     for i in p:
#         s.remove(i)
#     s.append(p)
#     s.sort()
#     for e in s:
#         res += e
#     print(res)

# for _ in range(int(input())):
#     s = list("akramkeeanany")
#     p = list("aka")
#     if all(i in s for i in p):


# for _ in range(int(input())):
#     s = input()
#     p = input()
#     s = list(s)
#     for x in p:
#         s.remove(x)
#     s = "".join(sorted(s))
#     if p[0] not in s:
#         s = "".join(sorted(s+p[0]))
#         n = s.rindex(p[0])
#         s = s[:n]+p+s[n+1:]
#     else:
#         n = s.rindex(p[0])
#         s = s[:n+1]+p+s[n+1:]
#     print(s)


# for _ in range(int(input())):
#     s = list("zaazyz")
#     p = "azy"
#     for x in p:
#         s.remove(x)
#     s = "".join(sorted(s))
#     i = 0
#     for x in p:
#         print(x, p[0])     ## 1.a  a   2.z  a
#         if x != p[0]:
#             print(x, p[0])          ## Loop out    z   a
#             if x < p[0]:
#                 i = 1
#             break
#     print(p[0], i)           ## p[0]=a   i=0
#     if p[0] not in s:         ## p[0]=a   s= zaazyz
#         s = "".join(sorted(s + p[0]))
#         if i == 0:
#             n = s.rindex(p[0])
#         else:
#             n = s.index(p[0])
#         s = s[:n] + p + s[n + 1:]
#     # print(s)                        #azz
#
#     else:
#         if i == 0:
#             # print(s.rindex(p[1]))
#             # print(s.index(p[1]))
#             n = s.rindex(p[0])
#         else:
#             n = s.index(p[0])
#         s = s[:n] + p + s[n:]
#     print(s)


t=int(input())
while t!=0:
    s=list(input().lower())
    p=input().lower()
    for i in p:
        s.remove(i)
    s.append(p)
    s.sort()
    # print(s)
    ind=s.index(p)
    # print(ind)
    if s[ind][1]<s[ind-1] and s[ind][0]==s[ind-1]:
        s[ind-1],s[ind]=s[ind],s[ind-1]
    # print(s)
    for i in s:
        print(i,end='')
    print()

    t-=1







