r, c = input().split()
r = int(r)
c = int(c)
count = 1
for i in range(r):
    for j in range(c - 1):
        print(count, end=" ")
        count += 1
    print(count, end="")
    print()
    count += 1