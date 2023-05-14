# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # index = tree level
        if not root:
            return []
        else:
            ans = []
            que = [root]
            while(que):
                tmp = []
                for i in range(len(que)):
                    x = que.pop(0)
                    tmp.append(x.val)
                    if (x.left):
                        que.append(x.left)
                    if (x.right):
                        que.append(x.right)
                print(tmp)
                ans.append(tmp)
            return ans
        
                
                
        