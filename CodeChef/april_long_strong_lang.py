for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    flag = 0
    i = 0
    for i in range(n):
        if s[i] == "*":
            flag += 1
            if flag >= k:
                print("YES")
                break
        else:
            flag = 0
    if flag < k:
        print("NO")



    # if s.count("*") < k or "*" not in s:
    #     print("NO")
    # elif "*" * k in s:
    #     print("YES")
    # else:
    #     print("NO")




    # temp = ""
    # li = []
    # for i in s:
    #     if i == "*":
    #         temp += i
    #     else:
    #         li.append(temp)
    #         temp = ""
    # if k == len(max(li)):
    #     print("YES")
    # else:
    #     print("NO")



    # for i in range(len(s)-1):
    #     if s[i] == "*":
    #         flag += 1
    #         if flag == k:
    #             print("YES")
    #             break
    #     else:
    #         flag = 0
    # if flag == 0:
    #     print("NO")