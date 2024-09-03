# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_node(node):
            nonlocal key
            if not node:
                return None
            if node.val == key:
                return delete_key(node)
            if node.val > key:
                node.left = find_node(node.left)
            else:
                node.right = find_node(node.right)
            return node
        
        def delete_key(node):
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # find min value in right subtree
            right = node.right
            while right.left:
                right = right.left
            node.val = right.val
            node.right = self.deleteNode(node.right, right.val)
            return node
            
        return find_node(root)