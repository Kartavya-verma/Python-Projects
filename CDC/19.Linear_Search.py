l = list(map(int,input().split()))
find_num = int(input())
f = 0
i = 0
for i in range(len(l)):
    if l[i] == find_num:
        f = 1
        break
if f == 1:
    print("Element Present at index:", i)
else:
    print("Element is not present")