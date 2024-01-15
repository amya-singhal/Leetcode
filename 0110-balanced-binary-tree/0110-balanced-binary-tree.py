# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True
        def height(root):
            nonlocal answer
            if not root:
                return 0
            else:
                leftH = height(root.left)
                rightH = height(root.right)
                if abs(leftH - rightH) > 1:
                    answer = False
                return max(leftH, rightH) + 1
        height(root)
        return answer