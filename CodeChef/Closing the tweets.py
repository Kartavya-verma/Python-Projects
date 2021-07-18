t=list(map(int,input().split()))
l = []
for i in range(t[1]):
    s=list(input().split())
    if(s[0]=="CLICK"):
        s[1] = int(s[1])
        if(s[1] not in l):
            l.append(s[1])
            print(len(l))
        else:
            l.remove(s[1])
            print(len(l))
    elif(s[0]=="CLOSEALL"):
        l.clear()
        print(len(l))
