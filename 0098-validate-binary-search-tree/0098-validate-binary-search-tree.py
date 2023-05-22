# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = -float('inf')
        maxi = float('inf')
        def recur(root, mini, maxi):
            if (not root):
                return True
            if (root.val > mini and root.val < maxi):
                if (root.right and root.left):
                    return recur(root.right, max(root.val, mini), maxi) and recur(root.left, mini, min(root.val, maxi))
                elif (root.right):
                    return recur(root.right, max(root.val, mini), maxi)
                elif (root.left):
                    return recur(root.left, mini, min(root.val, maxi))
                else:
                    return True
        return recur(root, mini, maxi)
            
        