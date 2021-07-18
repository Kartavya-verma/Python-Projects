x, y = input().split("=")
s = 0
for i in range(len(x)):
    s += int(x[i])
print(s)