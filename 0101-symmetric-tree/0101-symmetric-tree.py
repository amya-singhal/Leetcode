# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        qLeft = [root.left]
        qRight = [root.right]
        while(qRight and qLeft):
            x = qLeft.pop(0)
            y = qRight.pop(0)
            if (not x and not y):
                continue
            if (not x and y) or (x and not y):
                return False
            if (x.val != y.val):
                return False
            qLeft.append(x.left)
            qLeft.append(x.right)
            qRight.append(y.right)
            qRight.append(y.left)
        if (qRight or qRight):
            return False
        return True
        
        
#         def helper(leftR, rightR):
#             if (not leftR and not rightR):
#                 return True
#             if (not leftR and rightR) or (leftR and not rightR):
#                 return False
#             else:
#                 return (leftR.val == rightR.val) and helper(leftR.left, rightR.right) and helper(leftR.right, rightR.left)
#         return helper(root.left, root.right)
        