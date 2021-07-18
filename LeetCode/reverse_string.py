s = ["h","e","l","l","o"]
# print(s[::-1])
# s.reverse()
# print(s)

a = 0
b = len(s) - 1
while a < b:
    temp = s[a]
    s[a] = s[b]
    s[b] = temp
    a += 1
    b -= 1
print(s)