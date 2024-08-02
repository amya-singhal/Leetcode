# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            heappush(h, root.val)
            inorder(root.right)
        inorder(root)
        ans = -1
        for i in range(k):
            ans = heappop(h)
        return ans
        