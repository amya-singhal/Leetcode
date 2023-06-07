# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ansArray = []
        queue = [root]
        level = 0
        while queue:
            newQ = []
            ansArray.append(0)
            for q in queue:
                ansArray[level] = q.val
                if q.left:
                    newQ.append(q.left)
                if q.right:
                    newQ.append(q.right)
            queue = newQ
            level+=1
        return ansArray
        