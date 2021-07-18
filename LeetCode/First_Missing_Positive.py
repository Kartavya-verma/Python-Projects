class Solution:
    def firstMissingPositive(self, l: List[int]) -> int:
        i = 0
        while i < len(l):
            if 1 <= l[i] <= len(l) and l[i] != l[l[i] - 1]:
                temp = l[l[i] - 1]
                l[l[i] - 1] = l[i]
                l[i] = temp
            else:
                i += 1
        for i in range(len(l)):
            if i + 1 != l[i]:
                return i+1
        return len(l) + 1