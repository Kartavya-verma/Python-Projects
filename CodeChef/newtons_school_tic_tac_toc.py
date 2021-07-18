p1, p2 = input().split()
if p1 == "R" or p2 == "R":
    print("R")
elif p1 == "J":
    print(p2)
elif p2 == "J":
    print(p1)
else:
    print("D")