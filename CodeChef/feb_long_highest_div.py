n = int(input())
c = 0
for i in range(1,10):
    if n % i == 0:
        c = i
print(c)