# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = root.val
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.max = max(self.max, root.val + left + right, left+root.val, right+root.val)
            return max(left+root.val, right+root.val, root.val)
        dfs(root)
        return self.max