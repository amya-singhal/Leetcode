# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        n = {}
        def recur(root, n):
            if (not root):
                return n
            elif (root.val in n.keys()):
                n[root.val] += 1
            else:
                n[root.val] = 1
            if (root.left):
                recur(root.left, n)
            if (root.right):
                recur(root.right, n)
        recur(root, n)
        m = max(n.values())
        ans=[]
        for i in n.keys():
            if n[i] == m:
                ans.append(i)
        return ans
    