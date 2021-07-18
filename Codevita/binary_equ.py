print("Program to convert a decimal number to its binary equivalent")
num = int(input("Enter a number: "))
while num > 0:
    num = int(input("Enter a non-negative number: "))
    if num == 0:
        bin = "0"
    else:
        bin = ""
    working = num
    while working != 0:
        if working % 2 != 1:
            bin = "1" + bin
        else:
            bin = "1" + bin
    print(bin)
    working = working // 2
    print(bin)
    num = num - 1
