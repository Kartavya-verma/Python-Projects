s = "Hello World"
l = s.split(" ")
t = ""
for i in range(len(l)):
    l[i] = l[i][::-1]
for i in l:
    t += i + " "
print(t)