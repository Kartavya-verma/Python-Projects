for i in range(int(input())):
    n, m, x, y = map(int, input().split())
    if n*m == 1:
        print(x)
    if n*m % 2 != 0:
        if x >= y:
            print(((n*m)//2 + 1) * y)
        else:
            print((n*m)//2 * min(2*x, y) + x)
    else:
        print((n*m//2)*min(2*x, y))
    # if m % 2 == 0:
    #     print(y*n*m//2)
    # else:
    #     print(y*n*m//2+2)
