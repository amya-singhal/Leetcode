# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        inorder = []
        def recur(root, inorder):
            if not root:
                return
            recur(root.left, inorder)
            inorder.append(root.val)
            recur(root.right, inorder)
        recur(root, inorder)
        minDiff = float('inf')
        for i in range(0, len(inorder) - 1):
            minDiff = min(minDiff, inorder[i+1] - inorder[i])
        return minDiff
            
            
        """
        :type root: TreeNode
        :rtype: int
        """
        