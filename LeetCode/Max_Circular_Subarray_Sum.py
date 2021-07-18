def kadane(l):
    s1 = 0
    maxi = float('-inf')
    for i in range(len(l)):
        s1 += l[i]
        maxi = max(maxi,s1)
        if s1 < 0:
            s1 = 0
    return maxi


def circular_max(l):
    for i in range(len(l)):
        l[i] *= -1
    s = sum(l)
    sub = kadane(l)
    return max(s,-(s-sub)) if s > 0 else s


# l = [5,-3,-2,6,-1,4]
# l = [10,-3,-4,7,6,5,-4,-1]
l = [1,-2,3,-2]
print(circular_max(l))
