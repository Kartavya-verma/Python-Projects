for _ in range(int(input())):
    n = int(input())
    for num in range(1, n + 1):
        if num > 1:
            for i in range(2, int(n**0.5)+1):
                if (num % i) == 0:
                    break
            else:
                print(num)
