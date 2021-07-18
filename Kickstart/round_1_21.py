for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    flag = 0
    for i in range(1, n//2 + 1):
        if s[i-1] != s[(n-i)]:
            flag += 1
    if flag == k:
        print(0)
    else:
        print(flag)