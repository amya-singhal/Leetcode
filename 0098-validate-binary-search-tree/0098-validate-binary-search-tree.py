# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        mini = float('-inf')
        maxi = float('inf')
        def helper(root, maxi, mini):
            if not root:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            return helper(root.left, min(root.val, maxi), mini) and helper(root.right, maxi, max(root.val, mini))
        return helper(root, maxi, mini)
        