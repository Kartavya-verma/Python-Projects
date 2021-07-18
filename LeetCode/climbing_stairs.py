# Method 1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            res = 0
            while n > 2:
                res = a + b
                a = b
                b = res
        return res

# Method 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        results = [0] * (n + 1)
        results[0] = 0
        results[1] = 1
        results[2] = 2
        for i in range(3, n + 1):
            results[i] = results[i - 1] + results[i - 2]
        return results[n]