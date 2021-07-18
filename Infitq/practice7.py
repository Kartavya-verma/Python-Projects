s = input()
temp = []
c = 0
t = ''
for i in s:
    if i.isalnum():
       temp.append(i)
    else:
        c = s.index(i)
        t += i
print(temp, c)
temp.reverse()
temp.insert(c,t)
print(*temp)