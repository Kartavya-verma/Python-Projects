top=-1
def Push(stk,x):
    stk.append(x)
    top=len(stk)-1

def Pop(stk):
    if isEmpty(stk):
        return "under flow"
    else:
        x=stk.pop()
        if len(stk)==0:
            top=-1
        else:
            top=len(stk)-1
        return x

def isEmpty(a):
    if a==[]:
        return True
    else:
        return False

def matched(s):
    stk=[]
    for i in range(0,len(s)):
        if(s[i]=='('):
            Push(stk,s[i])
        elif(s[i]==')'):
            Pop(stk)
    if isEmpty(stk):
        print("True")
    else:
        print("False")
    return 0


matched("(7)(a")
matched("a)*(?")
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")