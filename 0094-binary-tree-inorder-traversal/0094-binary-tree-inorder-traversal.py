# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        def recur(root):
            nonlocal ans
            if root.left:
                recur(root.left)
            ans.append(root.val)
            if root.right:
                recur(root.right)
        recur(root)
        return ans