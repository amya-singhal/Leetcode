# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        cur = root
        def depth(root):
            nonlocal maxi
            if not root:
                return -1
            leftD = 1+depth(root.left)
            rightD = 1+depth(root.right)
            maxi = max(maxi, leftD+rightD)
            return max(leftD, rightD)
        depth(root)
        return maxi
        
        