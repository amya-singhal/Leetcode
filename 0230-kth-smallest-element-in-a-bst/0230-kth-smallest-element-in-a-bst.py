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
        heap = [1,2,3,4]
        1
        time complexity: n+klogn
        """
        heap = [] # [1,2,3,4]
        q = [root] # []
        while q:
            for _ in q:
                x = q.pop(0)
                if x is not None:
                    heapq.heappush(heap, x.val)
                    q.append(x.left)
                    q.append(x.right)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(heap)
        return ans