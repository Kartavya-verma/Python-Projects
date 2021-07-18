class Solution:
	def quadraticRoots(self, a, b, c):
            d = b * b - 4 * a * c
            sqrt_val = abs(d ** 0.5)
            return (-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a)

s = Solution()
print(s.quadraticRoots(1, -2, 1))