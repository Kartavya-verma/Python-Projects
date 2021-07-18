def armstrong(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i]) ** 3
    return int(n) == s


n = input()
print(armstrong(n))