n = int(input())
if n == 1 or n == 2:
    print("Prime")
else:
    f = 0
    for i in range(2, int(n**0.5)):
        if n % i == 0 and n != i:
            f = 1
            break
    if f == 1:
        print("Non-Prime")
    else:
        print("Prime")