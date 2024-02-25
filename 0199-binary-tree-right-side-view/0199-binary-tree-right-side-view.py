# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        def helper(root, level):
            nonlocal levels
            if not root:
                return
            levels[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        ans = []
        for i in range(len(levels)):
            ans.append(levels[i][-1])
        return ans
        