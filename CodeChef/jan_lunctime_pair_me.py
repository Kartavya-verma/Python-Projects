for _ in range(int(input())):
    x, y, z = map(int, input().split())
    l = [x, y, z]
    l.sort()
    if l[0] + l[1] == l[2]:
        print("YES")
    else:
        print("NO")