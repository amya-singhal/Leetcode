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
        d = defaultdict()
        for i in range(len(inorder)):
            d[inorder[i]] = i
        def helper(left, right):
            if left > right:
                return None
            element = preorder.popleft()
            root = TreeNode(element)
            x = d[element]
            root.left = helper(left, x-1)
            root.right = helper(x+1, right)
            return root
        preorder = deque(preorder)
        answer = helper(0, len(preorder)-1)
        return answer