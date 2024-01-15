# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        retVal = 0
        def longestPath(root):
            if not root:
                return 0
            nonlocal retVal
            left = longestPath(root.left)
            right = longestPath(root.right)
            tmpLongest = max(1 + left, 1 + right)
            retVal = max(1 + left + right, tmpLongest, retVal)
            return tmpLongest
        longestPath(root)
        return retVal-1