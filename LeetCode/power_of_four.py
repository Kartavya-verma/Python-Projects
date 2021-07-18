n = int(input())
b = str(bin(n).replace("0b", ""))
if n < 0:
    print("false")
else:
    if len(b) % 2 != 0 and b.count("1") == 1:
        print("true")
    else:
        print("false")