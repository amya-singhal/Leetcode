# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        q = [(root, 0)]
        while q:
            for _ in range(len(q)):
                node, level = q.pop(0)
                if not node:
                    continue
                levels[level].append(node.val)
                q.append((node.left, level+1))
                q.append((node.right, level+1))
        tmp = []
        for i in levels:
            tmp = levels[i]
        return tmp[0]
                
        