for _ in range(int(input())):
    c = int(input())
    bi = bin(c).replace("0b","")
    # print(bi)
    a = []
    b = []
    flag = 0
    for i in bi:
        # print(i,flag)
        if i == '1' and flag == 0:
            a.append(1)
            b.append(0)
            flag = 1
        elif i == '1' and flag == 1:
            a.append(0)
            b.append(1)
        elif i == '0':
            a.append(1)
            b.append(1)
    # print(a,b)
    # ai = int("".join(map(str, a)))
    # bi = int("".join(map(str, b)))
    ai = "".join(map(str, a))
    bi = "".join(map(str, b))
    # print(ai,bi)
    # print(int(ai,2),int(bi,2))
    print(int(ai,2)*int(bi,2))
