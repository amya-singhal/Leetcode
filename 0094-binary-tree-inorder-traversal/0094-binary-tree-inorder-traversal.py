# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        answer = []
        def recur(root):
            if not root:
                return
            else:
                recur(root.left)
                answer.append(root.val)
                recur(root.right)
        recur(root)
        return answer
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        