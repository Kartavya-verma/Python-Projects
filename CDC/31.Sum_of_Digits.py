def sum_digit(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s


n = input()
print(sum_digit(n))