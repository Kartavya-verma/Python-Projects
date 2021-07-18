for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    # print(l, r)
    res = []
    for i in range(len(l)):
        res.append(l[i]*r[i])
    # print(res)

    b = r.index(max(r))
    print(b)

    if b:
        a = res.index(max(res))
        print(a)

    # if res.index(max(res)) == r.index(max(r)):
    #     print(r.index(max(r)) + 1)