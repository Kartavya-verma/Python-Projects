num = input()
while(1):
    num = int(num) + int(num[::-1])
    num = str(num)
    if num == num[::-1]:
        print(num)
        break