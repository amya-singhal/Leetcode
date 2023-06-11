# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
                return False
        queue = [(root, targetSum - root.val)]
        while(queue):
            l = len(queue)
            x, y = queue.pop(0)
            if not x.right and not x.left and y == 0:
                return True
            if x.left:
                queue.append((x.left, y- x.left.val))
            if x.right:
                queue.append((x.right, y - x.right.val))
        return False