# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        q = [root]
        while q:
            l = len(q)
            for _ in range(l):
                x = q.pop(0)
                heappush(h, x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        ans = -1
        for i in range(k):
            ans = heappop(h)
        return ans
        