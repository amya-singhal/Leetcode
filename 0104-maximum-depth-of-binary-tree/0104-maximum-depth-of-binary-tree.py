# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        queue = [root]
        while(queue):
            l = len(queue)
            for i in range(l):
                x = queue.pop(0)
                if (x.left):
                    queue.append(x.left)
                if (x.right):
                    queue.append(x.right)
            level += 1
        return level
                
        