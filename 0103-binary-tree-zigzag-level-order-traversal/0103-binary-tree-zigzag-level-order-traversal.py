# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zigzag = 1
        queue = [root]
        ans = []
        while(queue):
            tmp = []
            l = len(queue)
            for i in range(l):
                # tmp = 1 queue = 3,2 tmp = 3,2 queue = 
                x = queue.pop(0)
                tmp.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            if zigzag:
                ans.append(tmp)
                zigzag = 0
            else:
                ans.append(tmp[::-1])
                zigzag = 1
        return ans