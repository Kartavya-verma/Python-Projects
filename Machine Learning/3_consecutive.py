st = input("Enter the string: ")
flag = 0
for i in range(len(st)-2):
    if (st[i] == '0' and st[i+1] == '0' and st[i+2] == '0') or (st[i] == '1' and st[i+1] == '1' and st[i+2] == '1'):
        print("Accepted")
        flag = 1
        break

if flag == 0:
    print("Rejected")