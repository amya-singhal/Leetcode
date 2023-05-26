# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        n = {}
        stack = []
        stack.append(root)
        while(stack):
            x = stack.pop()
            if x.val in n.keys():
                n[x.val] += 1
            else:
                n[x.val] = 1
            if (x.left):
                stack.append(x.left)
            if (x.right):
                stack.append(x.right)
        m = max(n.values())
        ans = []
        for i in n.keys():
            if n[i] == m:
                ans.append(i)
        return ans
    