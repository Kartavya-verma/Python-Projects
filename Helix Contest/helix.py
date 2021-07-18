for i in range(int(input())):
    s=input()
    c=0
    for j in range(len(s)-1):
        if(s[j]==s[j+1]):
            c=1
            break
    if(c==1):
        print("good")
    else:
        print("bad")