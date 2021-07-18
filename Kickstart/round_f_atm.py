def call(a):
    if all(j == 0 for j in a):
        return li
    else:
        for i in range(len(a)):
            if a[i] != 0:
                if a[i] <= x:
                    # print(i + 1)
                    # a.remove(i)
                    a[i] = 0
                    # print(a)
                    li.append(i + 1)
                else:
                    a[i] -= x
                    # print(a)
        call(a)


for j in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    li = []
    call(a)
    # print(li)
    print("Case" + " " + "#" + str(j+1) + ":",*li)


    # for i in a:
    #     print((i//x)+1)

