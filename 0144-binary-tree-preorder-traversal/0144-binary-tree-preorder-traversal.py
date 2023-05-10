# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recur(root):
            if(root):
                ans.append(root.val)
                recur(root.left)
                recur(root.right)
            return
        recur(root)
        return ans