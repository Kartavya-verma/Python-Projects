s = input()
# print(s[::-1])
s = list(s)
res = ""
st = 0
e = len(s)-1
for i in range(len(s)):
    if st <= e:
        s[st],s[e] = s[e],s[st]
        st += 1
        e -= 1
for i in s:
    res += i
print(res)
