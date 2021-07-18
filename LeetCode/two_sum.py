class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        result = []
        for index, num in enumerate(nums):
            if compliments.get(num) is None:
                compliments[target-num] = index
            else:
                result = [compliments[num], index]
        return result

l = Solution()
print()