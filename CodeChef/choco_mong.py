for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    s = len(set(l))
    sa = n - x
    if s > sa:
        print(sa)
    elif sa > s:
        print(s)
    elif s == sa:
        print(s)
