for i in range(int(input())):
    n = int(input())
    s = input()
    a = s.count('A')
    b = s.count('B')
    if abs(a-b) == 1 or abs(b-a) == 1:
        print("Case #"+str(i+1)+":", "Y")
    else:
        print("Case #"+str(i+1)+":", "N")

