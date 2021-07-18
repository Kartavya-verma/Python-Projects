for _ in range(int(input())):
    count = 0
    li = []
    n, k = map(int, input().split())
    for i in range(n):
        s, e = map(int, input().split())
        li.append(s)
        li.append(e)
    for j in range(len(li)):
        li[j] += k
        if