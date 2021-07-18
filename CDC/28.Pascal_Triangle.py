def print_pascal(l):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(l[i][j],end=" ")
        print()

def pascal(n):
    l = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(l[i-1][j]+l[i-1][j-1])
        l.append(temp)
    return print_pascal(l)

n = int(input())
pascal(n)
