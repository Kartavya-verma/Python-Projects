# n = input()
# l = 0
# for i in n:
#     # print(i)
#     if i == "(":
#         l += 1
#         print(l)
#     elif i == ")":
#         l -= 1
#         print(l)
# # print(l)

s = "{[]}"
if len(s) % 2 != 0:
    print("false")
else:
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{" :
            stack.append(c)
        elif len(stack) != 0 and c == ")" and stack[-1] == "(":
            stack.pop()
        elif len(stack) != 0 and c == "]" and stack[-1] == "[":
            stack.pop()
        elif len(stack) != 0 and c == "}" and stack[-1] == "{":
            stack.pop()
    print(len(stack) == 0)