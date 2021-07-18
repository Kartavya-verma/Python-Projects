for i in range(int(input())):
    s = input()
    sum1 = 0
    temp = s.count(s[0])
    for k in s:
        if s.count(k) > temp:
            temp = s.count(k)
    if temp == len(s)-temp:
        print("YES")
    else:
        print("NO")