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

        def bfs(node, level):
            if not node:
                return
            levels[level] = node.val
            bfs(node.left, level+1)
            bfs(node.right, level+1)
            
        # queue = [root]
        # level = 0
        # while queue:
        #     lenQ = len(queue)
        #     for _ in range(lenQ):
        #         x = queue.pop(0)
        #         levels[level] = x.val
        #         if x.left:
        #             queue.append(x.left)
        #         if x.right:
        #             queue.append(x.right)
        #     level += 1
        bfs(root, 0)
        rightSideList = []
        for i in range(len(levels)):
            rightSideList.append(levels[i])
        return rightSideList
            
                
        