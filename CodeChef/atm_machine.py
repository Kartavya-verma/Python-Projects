for i in range(int(input())):
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    s = ""
    for j in ai:
        if j <= k:
            k -= j
            s += "1"
            # print("k=",k,"j=",j,"s=",s)
        else:
            s += "0"
            # print("k=", k, "j=", j, "s=", s)
    print(s)