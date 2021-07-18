for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    y = [1]*n
    for x in range(n-2, -1, -1):
        if (l[x] > 0 and l[x+1] < 0) or (l[x] < 0 and l[x+1] > 0):
            y[x] += y[x+1]
    print(*y)