# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     c = 0
#     c1 = 0
#     count = {}
#     for i in a:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     print(count)
#
#     for i in range(n):
#         print(i, a[i], "li=2")
#         if c < count[a[i]]:
#             c = count[a[i]]
#             print(c, " mx ")
#
#         if c > (n+1) // 3:
#             print(c , n+1 , (n+1) % 3,"MX,%")
#             c1 += 1
#             break
#
#     if c1 == 0:
#         print("No")
#     else:
#         print("Yes")

    # for i in a:
    #     if i % 3 == 0:
    #         c += 1
    # if c % 2 == 0:
    #     print("Yes")
    # else:
    #     print("No")
    # print(c)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = 0
    o = 0
    t = 0
    for i in range(n):
        a[i] = a[i] % 3
        if a[i] == 0:
            z += 1
        elif a[i] == 1:
            o += 1
        else:
            t += 1
    if z == 0 and o != 0 and t != 0 :
        print('No')
    elif z == 0 and o != 0 and t == 0 :
        print("Yes")
    elif z == 0 and o == 0 and t == 0 :
        print("Yes")
    elif z <= o + t + 1:
        print("Yes")
    else:
        print("No")


