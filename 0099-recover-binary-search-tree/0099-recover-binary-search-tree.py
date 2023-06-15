# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorderTree = []
        stack = []
        while(root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorderTree.append(root)
            root = root.right
        sorted_order = sorted(inorderTree, key=lambda x:x.val)
        for i in range(len(inorderTree)):
            if inorderTree[i] != sorted_order[i]:
                inorderTree[i].val, sorted_order[i].val = sorted_order[i].val, inorderTree[i].val
                return
        
        
        
        """
        Do not return anything, modify root in-place instead.
        """
        