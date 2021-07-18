x = int(input())
if x >= 0:
    # print(int(str(x)[::-1]))
    a = int(str(x)[::-1])
else:
    x *= -1
    # print(-1 * int(str(x)[::-1]))
    a = -1 * int(str(x)[::-1])
if a not in range(-2**31, 2**31 - 1):
    print(0)
else:
    print(a)