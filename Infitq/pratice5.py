def fun(s):
    sta = []
    c = 0
    for i in s:
        if i == "(" or i == "[" or i == "{":
            sta.append(i)
            c += 1
            continue
        temp = sta.pop()
        if temp == "(" and i == ")":
            c += 1
        elif temp == "[" and i == "]":
            c += 1
        elif temp == "{" and i == "}":
            c += 1
        else:
            return c + 1
    if len(sta) == 0:
        return 0
    else:
        return c+1

a = input()
res = fun(a)
print(res)
























def fun(s):
    sta = []
    c = 0
    for i in s:
        if i == '[' or i == '(' or i == '{':
            sta.append(i)
            c += 1
            continue
        temp = sta.pop()
        if i == "}" and temp == "{":
            c += 1
        elif i == "]" and temp == "[":
            c += 1
        elif i == ")" and temp == "(":
            c += 1
        else:
            return c + 1
    if len(sta) == 0:
        return 0
    else:
        return c+1


inp = input()
res = fun(inp)
print(res)