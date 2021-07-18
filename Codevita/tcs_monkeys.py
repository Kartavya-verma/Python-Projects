for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l1 = [j+1 for j in range(len(l))]
    l2 = l1.copy()
    for j in range(len(l)):
        l2[l[j]-1] = l1[j]
    c = 1
    while True:
        for j in range(len(l)):
            l2[l[j] - 1] = l1[j]
            c = c + 1
        if l1 == l2:
            break
    print(c)