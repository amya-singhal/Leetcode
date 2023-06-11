# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(leftR, rightR):
            if (not leftR and not rightR):
                return True
            if (not leftR and rightR) or (leftR and not rightR):
                return False
            else:
                return (leftR.val == rightR.val) and helper(leftR.left, rightR.right) and helper(leftR.right, rightR.left)
        return helper(root.left, root.right)
        