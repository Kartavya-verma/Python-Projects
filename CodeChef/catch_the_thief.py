for _ in range(int(input())):
    x, y, k, n = input().split()
    x = int(x)
    y = int(y)
    k = int(k)
    if abs(x-y) % (2*k) == 0:
        print("Yes")
    else:
        print("No")