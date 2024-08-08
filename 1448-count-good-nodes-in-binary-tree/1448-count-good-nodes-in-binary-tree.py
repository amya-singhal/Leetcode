# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        goodNodes = 0
        
        def checkGoodNode(node, maxValue):
            nonlocal goodNodes
            if not node:
                return
            if node.val >= maxValue:
                goodNodes += 1
                maxValue = node.val
            checkGoodNode(node.left, maxValue)
            checkGoodNode(node.right, maxValue)
            return 
        
        maxValue = root.val
        checkGoodNode(root, maxValue)
        
        return goodNodes
        
        