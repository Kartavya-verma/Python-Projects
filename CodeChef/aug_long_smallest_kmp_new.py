# for _ in range(int(input())):
#     s = list("zzzety")
#     p = "ze"
#     c = 0
#     for x in p:
#         s.remove(x)
#     s = "".join(sorted(s))       ## s = tyzz
#     print(s)
#     for x in p:
#         if x != p[0]:
#             if x < p[0]:         ## x = e < p[0] = z
#                 c = 1
#             break
#     if p[0] in s:
#         if c == 0:
#             s = s[:s.rindex(p[0]) + 1] + p + s[s.rindex(p[0]) + 1:]
#         else:
#             s = s[:s.index(p[0])] + p + s[s.index(p[0]):]
#     else:
#         s = "".join(sorted(s + p[0]))
#         if c == 0:
#             n = s.rindex(p[0])
#         else:
#             n = s.index(p[0])
#         s = s[:n] + p + s[n + 1:]
#     print(s)

for _ in range(int(input())):
    s = input()
    p = input()
    s = list(s)
    for x in p:
        s.remove(x)
    s = "".join(sorted(s))
    i = 0
    for x in p:
        if x != p[0]:
            if x < p[0]:
                i = 1
            break

    if p[0] not in s:
        s = "".join(sorted(s + p[0]))
        if i == 0:
            n = s.rindex(p[0])
        else:
            n = s.index(p[0])
        s = s[:n] + p + s[n + 1:]

    else:
        if i == 0:
            n = s.rindex(p[0])
            s = s[:n + 1] + p + s[n + 1:]
        else:
            n = s.index(p[0])
            s = s[:n] + p + s[n:]
    print(s)