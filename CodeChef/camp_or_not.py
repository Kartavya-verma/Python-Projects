# for _ in range(int(input())):
#     dic = {}
#     cum = 0
#     for _ in range(int(input())):
#         day, prob = map(int, input().split())
#         cum = cum + prob
#         dic[day] = cum
#     print(dic)
#     dic1 = {}
#     for _ in range(int(input())):
#         dead, req = map(int, input().split())
#         dic1[dead] = req
#     print(dic1)

for _ in range(int(input())):
    days = []
    problems = []
    cum = 0
    for _ in range(int(input())):
        day, prob = map(int, input().split())
        days.append(day)
        cum = cum + prob
        problems.append(cum)
    print(problems)
    required = []
    for _ in range(int(input())):
        dead, req = map(int, input().split())
        temp = 0
        required.append(req)
    for i in range(len(required)):
        print(problems[i], required[i])
        if problems[i] >= required[i]:
            print("Go Camp")
        else:
            print("Go Sleep")
