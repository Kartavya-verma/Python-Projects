s = set(input())
for i in range(int(input())):
    st = input()
    c = 0
    for j in st:
        if j not in s:
            c = 1
            break
    if c == 0:
        print("Yes")
    else:
        print("No")
