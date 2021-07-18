n = int(input())
m = int(input())
s = 0
while True:
    if m > 0:
        s += n
        m -= 1
    else:
        break
print(s)