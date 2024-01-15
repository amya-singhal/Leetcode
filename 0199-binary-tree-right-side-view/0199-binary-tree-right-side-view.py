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
            if not root:
                return
            else:
                levels[level] += [root.val]
                helper(root.left, level+1)
                helper(root.right, level+1)
        helper(root, 0)
        print(levels)
        answer = []
        levelsList = levels.values()
        for l in levelsList:
            answer.append(l[-1])
        return answer