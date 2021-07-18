st = input("Enter the Regular Expression: ")

if len(st) < 3:
    print("Rejected")
elif st[-1] == "1" and st[-2] == "0" and st[-3] == "1":
    print("Accepted")
else:
    print("Rejected")