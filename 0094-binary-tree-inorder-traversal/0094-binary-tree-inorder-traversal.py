# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recur(root):
            nonlocal ans
            if not root:
                return
            recur(root.left)
            ans.append(root.val)
            recur(root.right)
        recur(root)
        return ans