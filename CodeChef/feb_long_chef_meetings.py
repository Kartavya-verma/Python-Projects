# for _ in range(int(input())):
#     p = input()
#     if p[6:]=='AM' and p[0:2]=='12':
#         p = '00'+p[2:]
#     elif p[6:]=='PM' and p[0:2]!='12':
#         p = str(int(p[0:2])+12)+p[2:]
#     #print(p)
#     n = int(input())
#     l = []
#     for i in range(n):
#         time = input()
#         h1 = int(time[0:2])
#         h2 = int(time[9:11])
#         if time[6:8]=='AM' and time[0:2]=='12':
#             h1 = '00'
#         if time[6:8]=='PM' and time[0:2]!='12':
#             h1 = str(h1+12)
#             if len(h1)<2:
#                 h1 = '0'+h1
#         if time[15:17]=='AM' and time[9:11]=='12':
#             h2 = '00'
#         if time[15:17]=='PM' and time[9:11]!='12':
#             h2 = str(h2+12)
#             if len(h2)<2:
#                 h2 = '0'+h2
#         l.append(str(h1)+time[2:9]+str(h2)+time[11:])
#     s = ''
#     for i in l:
#         if p[0:2]>= i[0:2] and p[0:2]<=i[9:11]:
#             if p[0:2]==i[0:2] and p[3:5]<i[3:5]:
#                 s+='0'
#             elif p[0:2]==i[9:11] and p[3:5]>i[12:14]:
#                 s+='0'
#             else:
#                 s+='1'
#         else:
#             s+='0'
#     print(s)


for _ in range(int(input())):
    p = input()
    if p[6:] == 'AM' and p[0:2] == '12':
        p = '00' + p[2:5]
    elif p[6:] == 'AM':
        p = p[:-2]
    elif p[6:] == 'PM' and p[0:2] != '12':
        p = str(int(p[0:2])+12)+p[2:5]
    else:
        p = p[:-2]
    n = int(input())
    l = []
    for i in range(n):
        time = input()
        h1 = time[0:8]
        h2 = time[9:17]
        if h1[6:8] == 'AM' and h1[0:2] == '12':
            h1 = '00' + h1[2:5]
        elif h1[6:8] == 'AM':
            h1 = h1[:-2]
        elif h1[6:8] == 'PM' and h1[0:2] != '12':
            h1 = str(int(h1[0:2]) + 12) + h1[2:5]
        else:
            h1 = h1[:-2]
        if h2[6:8] == 'AM' and h2[0:2] == '12':
            h2 = '00' + h2[2:5]
        elif h2[6:8] == 'AM':
            h2 = h2[:-3]
        elif h2[6:8] == 'PM' and h2[0:2] != '12':
            h2 = str(int(h2[0:2]) + 12) + h2[2:5]
        else:
            h2 = h2[:-2]
        l.append(h1+h2)
    s = ''
    for i in l:
        if i[0:2] < p[0:2] < i[6:8]:
            s += "1"
        elif i[0:2] == p[0:2]:
            if i[3:5] <= p[3:5]:
                s += "1"
            else:
                s += "0"
        elif i[6:8] == p[0:2]:
            if i[8:11] >= p[3:5]:
                s += "1"
            else:
                s += "0"
        else:
            s += "0"
    print(s)

for _ in range(int(input())):
    s = input()
    n = int(input())
    if s[6:] == 'AM' and s[0:2] == '12':
        s = '00' + s[2:5]
    elif s[6:] == 'AM':
        s = s[:-2]
    elif s[6:] == 'PM' and s[0:2] != '12':
        s = str(int(s[0:2]) + 12) + s[2:5]
    else:
        s = s[:-2]
    l = []
    for i in range(n):
        time = input()
        h1 = time[0:8]
        h2 = time[9:17]
        if h1[6:8] == 'AM' and h1[0:2] == '12':
            h1 = '00' + h1[2:5]
        elif h1[6:8] == 'AM':
            h1 = h1[:-3]
        elif h1[6:8] == 'PM' and h1[0:2] != '12':
            h1 = str(int(h1[0:2]) + 12) + h1[2:5]
        else:
            h1 = h1[:-3]
        if h2[6:8] == 'AM' and h2[0:2] == '12':
            h2 = '00' + h2[2:5]
        elif h2[6:8] == 'AM':
            h2 = h2[:-3]
        elif h2[6:8] == 'PM' and h2[0:2] != '12':
            h2 = str(int(h2[0:2]) + 12) + h2[2:5]
        else:
            h2 = h2[:-2]
        l.append(h1 + h2)

    s = ''
    for i in l:
        if p[0:2] >= i[0:2] and p[0:2] <= i[5:7]:
            if p[0:2] == i[0:2] and p[3:5] < i[3:5]:
                s += '0'
            elif p[0:2] == i[5:7] and p[3:5] > i[8:10]:
                s += '0'
            else:
                s += '1'
        else:
            s += '0'

    print(s)
