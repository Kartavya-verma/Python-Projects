s = input()
fi = ""
ele = s.split(",")
print(ele)

for i in ele:
    sub = i.split(":")
    name = sub[0]
    num = sub[1]
    max = 0
    for d in num:
        if(int(d) <= len(name)):
            if(max < int(d)):
                max = int(d)
    if max == 0:
        fi +='X'
    else:
        fi += name[max-1]
print(fi)