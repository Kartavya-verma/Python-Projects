for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(1, a+b+1, 2):
        a = a - j
        if a < 0:
            print("Bob")
            break
        b = b - (j+1)
        if b < 0:
            print("Limak")
            break