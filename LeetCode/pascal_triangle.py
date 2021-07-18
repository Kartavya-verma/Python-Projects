class Solution:
    def generate(self, numRows: int):
        tri = [[1] * i for i in range(1, numRows + 1)]
        i = 1
        while i < numRows:
            for j in range(1, len(tri[i-1])):
                tri[i][j] = tri[i-1][j] + tri[i-1][j-1]
            i += 1
        return tri


s = Solution()
s.generate(5)
# print(s.generate(5))