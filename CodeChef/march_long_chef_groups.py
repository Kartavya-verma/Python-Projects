# for _ in range(int(input())):
#     s = input()
#     c = 0
#     if s[0] == '1':
#         c += 1
#     for i in range(1, len(s)):
#         if s[i] == '1' and s[i-1] == '0':
#             c += 1
#     print(c)

for _ in range(int(input())):
    s = input()
    c = 0
    if s[-1] == '1':
        c += 1
    for i in range(len(s) - 1):
        if s[i] == '1' and s[i+1] == '0':
            c += 1
    print(c)