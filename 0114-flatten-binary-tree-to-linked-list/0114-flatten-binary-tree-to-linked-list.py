# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        while(root):
            if root.left:
                x = root.left
                while x.right:
                    x = x.right
                x.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
                    
            
        """
        Do not return anything, modify root in-place instead.
        """
        