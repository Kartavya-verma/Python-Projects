import math
for i in range(int(input())):
    t=math.ceil(int(input())/2)
    c=0
    for num in range(t+1):
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                c+=1
    print(c+1)