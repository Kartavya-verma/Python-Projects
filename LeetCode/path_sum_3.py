# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total = 0

    def pathsum(self, root: TreeNode, sum: int):
        if root == None:
            return 0
        global hm
        hm = {}
        hm[0] = 1
        findPathSum(root, 0, sum, hm)
        return self.total

    def findPathSum(self, curr: TreeNode, sum, target, hm):
        if curr == None :
            return
        sum += curr.val;
        if hm.containsKey(sum - target):
            self.total += hm.get(sum - target)
        hm.put(sum, hm.getOrDefault(sum, 0) + 1)
        findPathSum(curr.left, sum, target, hm)
        findPathSum(curr.right, sum, target, hm)

    hm.put(sum, hm.get(sum) - 1)
    return
