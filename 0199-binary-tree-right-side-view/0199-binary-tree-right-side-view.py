# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q =[root]
        while q:
            ans.append(q[-1].val)
            for _ in range(len(q)):
                x = q.pop(0)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)       
        return ans
        