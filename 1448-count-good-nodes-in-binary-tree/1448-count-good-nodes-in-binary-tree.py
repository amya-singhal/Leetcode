# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, float('-inf'))]
        while stack:
            node, maxNum = stack.pop()
            if not node:
                continue
            if node.val >= maxNum:
                ans += 1
            stack.append((node.left, max(maxNum, node.val)))
            stack.append((node.right, max(maxNum, node.val)))
        return ans
                