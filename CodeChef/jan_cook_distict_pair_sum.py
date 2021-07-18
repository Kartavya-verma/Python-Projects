for _ in range(int(input())):
    l, r = map(int,input().split())
    c = 0
    # n = r - l
    # print(2*n + 1)
    for i in range(l,r+1):
        for j in range(i,r+1):
            # print("i", i)
            # print("j", j)
            # print(i+j)
            c += 1
    print(c)