# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def helper(root):
            nonlocal ans
            if not root:
                return 0, 0
            sumT, count = root.val, 1
            
            sumTLeft, countLeft = helper(root.left)
            sumTRight, countRight = helper(root.right)
            sumT += (sumTLeft + sumTRight)
            count += (countLeft + countRight)
            
            
            if count > 0 and sumT // count == root.val:
                    ans += 1
            return sumT, count
        
        helper(root)
        return ans
            
            