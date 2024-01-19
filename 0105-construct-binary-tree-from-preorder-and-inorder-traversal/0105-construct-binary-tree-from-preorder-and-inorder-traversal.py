# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #  r [20,15,7] l [15,7] r [7] 
        #  r [15,20,7] l [15] r [7]
        # root = [3,9,None,None,20,15, None, None,7, None, None]
        def helper(root, preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            index = 0
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    index = i
                    break
            root.left = helper(root.left, preorder[1:i+1], inorder[:i])
            root.right = helper(root.right, preorder[i+1:], inorder[i+1:])
            return root
        answer = helper(None, preorder, inorder)
        return answer