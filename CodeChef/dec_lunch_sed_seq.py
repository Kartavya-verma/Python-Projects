for _ in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    l = map(int, input().split())
    if sum(l) % k == 0:
        print(0)
    else:
        print(1)
