# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def helper(root, maxi):
            nonlocal ans
            if not root:
                return
            if root.val >= maxi:
                ans += 1
            helper(root.left, max(maxi, root.val))
            helper(root.right, max(maxi, root.val))
            return
        helper(root, root.val)
        return ans