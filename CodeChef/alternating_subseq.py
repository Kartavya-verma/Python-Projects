for j in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    o = [1] * n
    for i in range(n - 2, -1, -1):
        if (a[i] < 0 and a[i + 1] > 0) or (a[i] > 0 and a[i + 1] < 0):
            o[i] += o[i + 1]
    print(*o)