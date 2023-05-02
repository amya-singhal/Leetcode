# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if (not root):
            return []
        answer = []
        def recur(root, validPath):
            if (not root):
                return
            if (not root.right and not root.left):
                validPath.append(root.val)
                if (sum(validPath) == targetSum):
                    answer.append(validPath)
                return
            recur(root.left, validPath+[root.val])
            recur(root.right, validPath+[root.val])
        recur(root, [])
        return answer
            
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        