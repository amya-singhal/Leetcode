# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        [3,1,4,null,2]
        k = 1
        ordered = [1, 2, 3, 4]
        """
        ordered = []
        def dfs(root):
            nonlocal ordered
            if not root:
                return
            dfs(root.left)
            ordered.append(root.val)
            dfs(root.right)
        dfs(root)
        # [1,2,3,4]
        return ordered[k-1]
            
        