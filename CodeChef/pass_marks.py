for _ in range(int(input())):
    l = list(map(int, input().split()))
    if l[4] >= l[0] and l[5] >= l[1] and l[6] >= l[2]:
        if l[4]+l[5]+l[6] >= l[3]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")