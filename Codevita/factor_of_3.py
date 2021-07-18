def distantAdjacentElement(a, n):
    m = dict()
    c = 0
    mx = 0
    for i in range(n):
        # print(i, a[i], "li=1")
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    # print(m, "m=1")

    for i in range(n):
        print(i, a[i], "li=2")
        if mx < m[a[i]]:
            mx = m[a[i]]
            print(mx, " mx ")

        if mx > (n+1) // 3:
            # print(mx , n+1 , (n+1) % 3,"MX,%")
            c += 1
            break
    return c


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = distantAdjacentElement(a, n)
    if res == 0:
        print("No")
    else:
        print("Yes")