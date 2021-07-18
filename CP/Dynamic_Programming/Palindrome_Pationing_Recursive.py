def isPalindrome(x):
    return x == x[::-1]


def minPalPartion(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    mn = float('inf')
    for k in range(i, j):
        temp = (1 + minPalPartion(string, i, k) + minPalPartion(string, k + 1, j))
        if temp < mn:
            mn = temp
    return mn


string = "ababbbabbababa"
print(minPalPartion(string, 0, len(string) - 1))
