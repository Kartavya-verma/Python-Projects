for _ in range(int(input())):
    n, k, x, y = map(int,input().split())
    for i in range(k):
        x += k
        y += k
        if x > n or y > n:
            print()