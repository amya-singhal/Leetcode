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
        levels = defaultdict(int)
        queue = [root]
        level = 0 # 1, 2
        # [1], [2,3]
        # {0: [1], 1: [2, 3], 2: [5, 4] }
        # [1,2,3,null,5,null,4]
        while queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                x = queue.pop(0)
                levels[level] = x.val
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            level += 1
        rightSideList = []
        for i in range(level):
            rightSideList.append(levels[i])
        return rightSideList
            
                
        