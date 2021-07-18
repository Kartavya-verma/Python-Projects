def lcs(l):
    l = set(l)
    print(l)
    c = 0
    for i in l:
        if i - 1 not in l:
            y = i + 1
            while y in l:
                y += 1
            c = max(c, y - i)
    return (c)


l = list(map(int,input().split()))
print(lcs(l))