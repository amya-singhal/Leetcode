# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ansArray = []
        stack = []
        curr = root
        level = 0
        while(stack or curr):
            while(curr):
                if (level >= len(ansArray)):
                    ansArray.append(-1)
                stack.append((curr, level))
                curr = curr.left
                level+=1
            # print(stack)
            curr,level = stack.pop()
            ansArray[level] = curr.val
            
            curr = curr.right
            level+=1
        
        return ansArray
        