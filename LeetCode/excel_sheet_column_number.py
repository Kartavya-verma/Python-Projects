result = 0
s = "zbd".upper()
for c in s:
    # print(c,"=",ord(c))
    d = ord(c) - ord('A') + 1
    result = result*26 + d
print(result)