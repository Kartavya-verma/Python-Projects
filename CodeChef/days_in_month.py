for _ in range(int(input())):
    w, s = input().split()
    w = int(w)
    l = [0] * 7
    if s == "mon":
        d = 0
    elif s == "tues":
        d = 1
    elif s == "wed":
        d = 2
    elif s == "thurs":
        d = 3
    elif s == "fri":
        d = 4
    elif s == "sat":
        d = 5
    elif s == "sun":
        d = 6
    for i in range(1, w+1):
        l[d] += 1
        d += 1
        if d == 7:
            d = 0
    print(*l)