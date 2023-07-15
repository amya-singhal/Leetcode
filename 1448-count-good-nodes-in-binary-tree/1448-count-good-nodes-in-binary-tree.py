# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 0
        def helper(root, maxi):
            if not root:
                return
            nonlocal good
            if root.val >= maxi:
                good += 1
                maxi = root.val
            helper(root.left, maxi)
            helper(root.right, maxi)
        helper(root, root.val)
        return good