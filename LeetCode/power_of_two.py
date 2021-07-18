n = int(input())
c = 0
while n > 0:
    c += 1
    n = n & (n-1)
if c == 1:
    print("true")
else:
    print("false")