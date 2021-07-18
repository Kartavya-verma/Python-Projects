s = "geeksforgeeks"
res = []
for i in list(set(s)):
    if s.count(i) > 1:
        res.append(i)
print(*res)