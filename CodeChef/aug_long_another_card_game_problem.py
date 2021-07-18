from math import ceil
for _ in range(int(input())):
    pc, pr = map(int, input().split())
    if ceil(pr/9) <= ceil(pc/9):
        print(1, ceil(pr/9))
    else:
        print(0, ceil(pc/9))