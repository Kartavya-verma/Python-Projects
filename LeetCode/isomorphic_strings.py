if len(s) != len(t):
    return False
s1 = {}
t1 = {}
for i in range(len(s)):
    if s[i] not in s1:
        s1[s[i]] = t[i]
    if t[i] not in t1:
        t1[t[i]] = s[i]
    if t1[t[i]] != s[i] or s1[s[i]] != t[i]:
        return False
return True