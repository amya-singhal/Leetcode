# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        preorder = []
        preorder.append(root.val)
        def helper(root):
            if not root:
                return
            preorder.append(root.val)
            helper(root.left)
            helper(root.right)
            # root = None
        helper(root.left)
        helper(root.right)
        # print(preorder)
        while(preorder):
            # if not root:
            #     root = TreeNode()
            root.val = preorder[0]
            root.left = None
            if not root.right and len(preorder) > 1:
                root.right = TreeNode()
            root = root.right
            preorder = preorder[1:]
        # print(root)
            
        """
        Do not return anything, modify root in-place instead.
        """
        