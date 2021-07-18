from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root)
        gpby = defaultdict(list)
        def dfs(node, x, y):
            gpby[x].append((y, node.val))
            if node.left: dfs(node.left, x-1, y+1)
            if node.right: dfs(node.right, x+1, y+1)
        dfs(root,0,0)
        return [[t[1] for t in sorted(gpby[x])] for x in sorted(gpby)]


s = Solution()
s.verticalTraversal()