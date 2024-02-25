# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        queue = [(root, 0)]
        ans = []
        while queue:
            l = len(queue)
            for _ in range(l):
                node, level = queue.pop(0)
                if not node:
                    continue
                levels[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        for i in range(len(levels)):
            ans.append(levels[i][-1])
        return ans
        