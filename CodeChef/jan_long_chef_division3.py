for _ in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) // k > d:
        print(d)
    else:
        print(sum(a) // k)