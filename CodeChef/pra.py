def repeat(s):
    prefix_array=[]
    for i in range(len(s)):
        prefix_array.append(s[:i])

    for i in prefix_array[:1:-1]:
        if s.count(i) > 1 :
            offset = s[len(i):].find(i)
            return s[:len(i)+offset]
            break
    return s

s="ababab"
temp=repeat(s)
if temp in s and s!=temp:
    print(1)
else:
    print(0)