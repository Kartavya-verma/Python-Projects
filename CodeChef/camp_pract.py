for _ in range(int(input())):
    days = [0] * 32
    for __ in range(int(input())):
        d, p = map(int, input().split())
        days[d] = p
    for i in range(1, 32):
        days[i] += days[i - 1]
    # print(days)
    for ___ in range(int(input())):
        dead, req = map(int, input().split())
        # print(days[d], p)
        if days[dead] >= req:
            print("Go Camp")
        else:
            print("Go Sleep")