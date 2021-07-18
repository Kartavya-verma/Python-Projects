for _ in range(int(input())):
    n = int(input())
    c = 0
    while n > 0:
        c += 1
        n = n & (n-1)
    print(c)