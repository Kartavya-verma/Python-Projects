from math import sqrt
t=int(input())
for i in range(t):
    r = int(input())
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x3, y3 = list(map(int, input().split()))
    d1 = sqrt((x1-x2)**2 + (y1-y2)**2)
    d2 = sqrt((x2-x3)**2 + (y2-y3)**2)
    d3 = sqrt((x1-x3)**2 + (y1-y3)**2)
    count = 0
    if d1 <= r:
        count += 1
    if d2 <= r:
        count += 1
    if d3 <= r:
        count += 1
    if count >= 2:
        print('yes')
    else:
        print('no')