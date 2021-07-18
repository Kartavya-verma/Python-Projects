def matched(s):
    count=0
    sum=0
    i=len(s)
    for i in range(0,len(s)):
        if(s[i]=='('):
            count+=1
        elif(s[i]==')'):
            sum+=1

    if(count==sum):
        print("True")
    else:
        print("False")
    return 0


matched("(7)(a")
matched("a)*(?")
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
