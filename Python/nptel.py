def intreverse(Number):
    Reverse = 0
    while (Number > 0):
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        Number = Number // 10
    return Reverse


intreverse(368)
intreverse(798798)
intreverse(7)

top = -1


def Push(stk, x):
    stk.append(x)
    top = len(stk) - 1


def Pop(stk):
    if isEmpty(stk):
        return "under flow"
    else:
        x = stk.pop()
        if len(stk) == 0:
            top = -1
        else:
            top = len(stk) - 1
        return x


def isEmpty(a):
    if a == []:
        return True
    else:
        return False


def matched(s):
    stk = []
    for i in range(0, len(s)):
        if (s[i] == '('):
            Push(stk, s[i])
        elif (s[i] == ')'):
            Pop(stk)
    if isEmpty(stk):
        return True
    else:
        return False
    return 0


matched("(7)(a")
matched("a)*(?")
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")


def sumprimes(l):
    sum = 0

    for i in range(0, len(l)):
        flag = 1
        if (l[i] == 2):
            sum = sum + 2
        else:
            for j in range(2, l[i]):
                if (l[i] % j == 0):
                    flag = 0
            if (flag == 1):
                sum = sum + l[i]
    return sum


sumprimes([17, 51, 29, 39])
sumprimes([-3, -5, 3, 5])
sumprimes([4, 6, 15, 27])