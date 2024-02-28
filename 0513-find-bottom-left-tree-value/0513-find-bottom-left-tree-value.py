# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        def helper(root, level):
            if not root:
                return
            levels[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        tmp = []
        for i in levels:
            tmp = levels[i]
        return tmp[0]
                
        