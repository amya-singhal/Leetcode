# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(l, r):
            trees = []
            if l > r:
                trees.append(None)
            for i in range(l, r+1):
                left = helper(l, i-1)
                right = helper(i+1, r)
                for x in left:
                    for y in right:
                        root = TreeNode(i)
                        root.left = x
                        root.right = y
                        trees.append(root)
            return trees
        return helper(1, n)
        