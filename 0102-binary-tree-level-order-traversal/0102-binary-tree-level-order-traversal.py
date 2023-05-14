# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # index = tree level
        ans = []
        level = 0
        def recur(root, level):
            if (root):
                if(len(ans) < level + 1):
                    ans.append([])
                ans[level].append(root.val)
                recur(root.left, level+1)
                recur(root.right, level+1)
            return
        recur(root, level)
        return ans
        