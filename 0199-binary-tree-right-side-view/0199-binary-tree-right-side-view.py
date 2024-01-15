# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        q = [root]
        x = 0
        while q:
            for i in range(len(q)):
                element = q.pop(0)
                if not element:
                    continue
                levels[x] += [element.val]
                q.append(element.left)
                q.append(element.right)
            x += 1
        print(levels)
        answer = []
        levelsList = levels.values()
        for l in levelsList:
            answer.append(l[-1])
        return answer