# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        not_balanced = False
        def check_height(node):
            nonlocal not_balanced
            if not node:
                return 0
            left = 1 + check_height(node.left)
            right = 1+ check_height(node.right)
            # print(left, right)
            if abs(left-right) > 1:
                not_balanced = True
            return max(left, right)
        
        check_height(root)
        return not not_balanced