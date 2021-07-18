def isPalindrome(x):
    return x == x[::-1]


def minPalPartion(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    if t[i][j] != -1:
        return t[i][j]
    mn = float('inf')
    for k in range(i, j):
        temp = (1 + minPalPartion(string, i, k) + minPalPartion(string, k + 1, j))
        if temp < mn:
            mn = temp
        t[i][j] = mn
    return t[i][j]


string = "ababbbabbababa"
t = [[-1 for i in range(1001)]for y in range(1001)]
print(minPalPartion(string, 0, len(string) - 1))
