for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    li = list(map(int, input().split()))
    c = 0
    for j in li:
        j = j + k
        if j % 7 == 0:
            c = c + 1
    print(c)