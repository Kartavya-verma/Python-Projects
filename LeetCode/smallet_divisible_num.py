import math
class Solution:
    def getSmallestDivNum(self, n):
        # code here def lcm(n):
        ans = 1
        for i in range(1, n + 1):
            ans = int((ans * i)/math.gcd(ans, i))
            print(ans)
        return ans
s = Solution()
s.getSmallestDivNum(5)