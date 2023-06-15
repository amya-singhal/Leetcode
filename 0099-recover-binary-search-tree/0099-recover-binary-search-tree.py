# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder = []
        inorderTree = []
        stack = []
        while(root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            inorderTree.append(root)
            root = root.right
        inorder.sort()
        for i in range(len(inorder)):
            inorderTree[i].val = inorder[i]
        
        
        """
        Do not return anything, modify root in-place instead.
        """
        