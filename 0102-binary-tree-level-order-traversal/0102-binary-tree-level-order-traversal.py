# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        while(queue):
            tmp = []
            l = len(queue)
            for i in range(l):
                x = queue.pop(0)
                tmp.append(x.val)
                if (x.left):
                    queue.append(x.left)
                if (x.right):
                    queue.append(x.right)
            ans.append(tmp) 
        return ans
        
            