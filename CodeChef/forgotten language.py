for i in range(int(input())):
    n, k = map(int, input().split())
    a = input().split()
    res = ['NO']*(n)
    for j in range(k):
        s = input().split()
        s = s[1:]
        for j in s:
            if j in a:
                res[a.index(j)] = 'YES'
    print(' '.join(res))