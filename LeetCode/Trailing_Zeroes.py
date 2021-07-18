def trailing(n):
    temp = 0
    while n > 0:
        n //= 5
        temp += n
    return temp


n = int(input())
print(trailing(n))