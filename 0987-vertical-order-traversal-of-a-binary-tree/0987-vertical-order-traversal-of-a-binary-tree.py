# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = []
        def bfs(root, val, level):
            if not root:
                return
            positions.append([val, level, root.val])
            bfs(root.left, val-1, level+1)
            bfs(root.right, val+1, level+1)
        bfs(root, 0, 0)   
        positions.sort()
        # print(positions)
        q = positions[0][0]
        # print(q)
        tmp = []
        ans = []
        for x,y, node in positions:
            if x == q:
                tmp.append(node)
            else:
                ans.append(tmp)
                tmp = [node]
                q = x
        if len(tmp) != 0:
            ans.append(tmp)
        return ans
                
                
                
                
            