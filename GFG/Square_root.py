def square(n):
    s, e = 1, n
    ans = 0
    while s <= e:
        mid = s + (e-s)//2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            e = mid - 1
        elif mid * mid < n:
            ans = mid
            s = mid + 1
    return ans


n = 16
print(square(n))