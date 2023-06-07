# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ansArray = []
        def dfs(root, level):
            nonlocal ansArray
            if root == None: return
            elif (len(ansArray) == level):
                ansArray.append(root.val)
            else:
                ansArray[level] = root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
                
        dfs(root, 0)
        return ansArray
        