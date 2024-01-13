# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxi = float('inf')
        mini = float('-inf')
        def helper(root, maxi, mini):
            if not root:
                return True
            if root.val < maxi and root.val > mini:
                return helper(root.left, min(maxi, root.val), mini) and helper(root.right, maxi, max(mini, root.val))
            else:
                return False
        return helper(root, maxi, mini)
            
                