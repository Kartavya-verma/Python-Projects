for _ in range(int(input())):
    n = int(input())
    li = [1,2,3,4,5,6]
    if n == 1:
        print(20)
    elif n == 2:
        print(36)
    elif n == 3:
        print(51)
    elif n == 4:
        print(60)
    elif n>4:
        k = n % 4
        if k == 1:

    li.remove(n)
    print(sum(li))