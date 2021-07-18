for _ in range(int(input())):
    b = 0
    mx = 0
    for i in input():
        if i == "(":
            b += 1
        else:
            b -= 1
        mx = max(b,mx)
    print("("*mx + ")"*mx)


# for _ in range(int(input())):
#     s = input()
#     mx = 1
#     count = 0
#     for i in range(len(s) - 1):
#         if s[i] == s[i+1]:
#             mx += 1
#         else:
#             if mx > count:
#                 count = mx
#             mx = 1
#     print("("*mx + ")"*mx)

for _ in range(int(input())):
    s = input()
    mx = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
            mx = max(mx, count)
        else:
            count = 0
    print("("*mx + ")"*mx)