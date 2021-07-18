class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        a = 0
        b = 1
        sum1 = 0
        while N > 1:
            sum1 = a + b
            a = b
            b = sum1
            N -= 1
        return sum1