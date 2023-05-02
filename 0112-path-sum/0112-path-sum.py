# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if (not root):
            return False
        currentSum = 0
        def recur(root, targetSum, currentSum):
            if (not root):
                return False
            if (not root.right and not root.left):
                currentSum += root.val
                if (currentSum == targetSum):
                    return True
                else:
                    return False
            while (root):
                currentSum += root.val
                return recur(root.left, targetSum, currentSum) or recur(root.right, targetSum, currentSum)
        return recur(root, targetSum, currentSum)
        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        