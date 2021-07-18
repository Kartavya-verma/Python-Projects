s = input()

if len(s) % 2 != 0:
    print("Invalid")
    exit()

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
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")