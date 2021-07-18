def bc(x, y):
    x = bin(x).replace("0b", "")
    y = bin(y).replace("0b", "")

    sumx = x + y
    sumy = y + x

    xsumy = int(sumx, 2)
    ysumx = int(sumy, 2)

    return xsumy-ysumx


for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set()
    # if n <= 500:
    #     for j in range(len(l)):
    #         for k in range(len(l)):
    #             s.add(abs(bc(l[j], l[k])))
    #     print(max(s))
    # else:
    temp = max(l)
    for x in range(len(l)):
        s.add(bc(temp, l[x]))
    print(max(s))