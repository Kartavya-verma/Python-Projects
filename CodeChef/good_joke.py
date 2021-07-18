for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        input()
        ans = ans ^ i
        # print(ans,"^",i,":",ans^i)
    print(ans)