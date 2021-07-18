i = int(input())
while i != 0:
    f = 0
    n = int(input())
    s = input()
    l = set(s)
    for j in l:
        if s.count(j) % 2 !=0:
            f = 1
    if f ==1:
        print("NO")
    else:
        print("YES")
    i = i-1

# i = int(input())
# while i != 0:
#     n = int(input())
#     if n % 2 != 0:
#         print("NO")
#     else:
#
#
#     i = i-1