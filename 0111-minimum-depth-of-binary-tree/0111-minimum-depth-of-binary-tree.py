# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = float('inf')
        def recur(root, level):
            nonlocal ans
            if not root.left and not root.right:
                return level+1
            if root.left:
                x = recur(root.left, level+1)
                ans = min(ans, x)
            if root.right:
                y = recur(root.right, level+1)
                ans = min(ans, y)
            return ans
        return recur(root, 0)