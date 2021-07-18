for _ in range(int(input())):
    c = 0
    a ,b ,n = map(int, input().split())
    if n % 2 == 0:
        pass
    else:
        a *= 2
    if a > b:
        print(a // b)
    else:
        print(b // a)