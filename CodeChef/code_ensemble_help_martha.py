for _ in range(int(input())):
    s = list(input())
    x, y = map(int, input().split())
    q = int(input())
    # d = {"R": s.count("R"), "L": s.count("L"), "U": s.count("U"), "D": s.count("RD")}
    # print(d)
    for _ in range(q):
        x1, y1 = map(int, input().split())
        for i in s:
            if i == "R":
                x += 1
                s.remove("R")
            elif i == "L":
                x -= 1
                s.remove("L")
            elif i == "U":
                y += 1
                s.remove("U")
            elif i == "D":
                y -= 1
                s.remove("D")
            print(x, y)