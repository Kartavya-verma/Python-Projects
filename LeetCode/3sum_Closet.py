def three_sum(li,t):
    li.sort()
    res = sum(li[:3])
    for i in range(len(li)):
        l, r = i+1, len(li)-1
        while l < r:
            s = sum((li[i], li[l], li[r]))
            if abs(s-t) < abs(res-t):
                res = s
            if s < t:
                l += 1
            elif s > t:
                r -= 1
            else:
                return res
    return res


l = [5,2,7,5]
t = 13
print(three_sum(l,t))