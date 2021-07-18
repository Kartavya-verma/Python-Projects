pattern = "abba"
s = "dog cat cat dog"
# print(len(list(s)))
t = s.split()
# print(t)
if len(pattern) != len(t):
    print("False")
s1 = {}
t1 = {}
for i in range(len(pattern)):
    if pattern[i] not in s1:
        s1[pattern[i]] = t[i]
    if t[i] not in t1:
        t1[t[i]] = pattern[i]
    if t1[t[i]] != pattern[i] or s1[pattern[i]] != t[i]:
        print("False")
print("True")