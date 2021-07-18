# for i in range(int(input())):
#     n = int(input())
#     li = list(map(int, input().split()))
#     li1 = list(map(int, input().split()))
#     li.insert(0, 0)
#     li1.insert(0, 0)
#     temp = 0
#     temp1 = 0
#     c = 0
#     for j in range(len(li)-1):
#         temp = li[j+1] - li[j]
#         temp1 = li1[j+1] - li1[j]
#         if abs(temp) == abs(temp1):
#             c += 1
#         print("Temp = ", temp)
#         print("Temp1 = ", temp1)
#     print(c)

for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li1 = list(map(int, input().split()))
    li.insert(0, 0)
    temp = 0
    c = 0
    for j in range(len(li)-1):
        temp = li[j+1] - li[j]
        # print(temp,li1[j])
        if li1[j] <= temp:
            c += 1
        # if abs(temp) > li1[j]:
        #     c += 1
        # print("Temp = ", temp)
        # print("Temp1 = ", temp1)
    print(c)














