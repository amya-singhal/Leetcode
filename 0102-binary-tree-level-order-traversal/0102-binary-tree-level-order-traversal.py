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
            print(l)
            for i in range(l):
                if not queue[0]:
                    queue.pop(0)
                    continue
                print("x")
                tmp.append(queue[0].val)
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                queue.pop(0)
            if tmp:
                ans.append(tmp) 
            print(ans)
        return ans
        
            