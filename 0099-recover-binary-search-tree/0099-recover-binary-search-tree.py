# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        start = None
        end = None
        def dfs(root):
            nonlocal prev, start, end
            if not root:
                return
            dfs(root.left)
            if prev and prev.val > root.val:
                if not start:
                    start = prev
                end = root
            prev = root
            dfs(root.right)
        dfs(root)
        if start and end:
            start.val, end.val = end.val, start.val
            
        
        """
        Do not return anything, modify root in-place instead.
        """
        