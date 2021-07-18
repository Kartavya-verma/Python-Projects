t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    sublist = []
    b = []
    for i in range(len(l) + 1):
        for j in range(i + 1, len(l) + 1):
            sub = l[i:j]
            sublist.append(sub)

    for i in sublist:
        p = 0
        for j in i:
            p = p | j
        b.append(p)

    if len(b) != len(set(b)):
        print("NO")
    else:
        print("YES")
    t -= 1