# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = [] # index, level, value of node
        def bfs(root, level, index):
            if not root:
                return
            array.append([index, level, root.val])
            bfs(root.left, level+1, index-1)
            bfs(root.right, level+1, index+1)
        bfs(root, 0, 0)
        array.sort()
        # [[-1,1,9] [0,0,3] [0,2,15]...]
        q = array[0][0]
        tmp = []
        verticalTraversal = []
        for i, l, node in array:
            if i == q:
                tmp.append(node)
            else:
                verticalTraversal.append(tmp)
                q = i
                tmp = [node]
        if len(tmp) != 0:
            verticalTraversal.append(tmp)
        # tmp = [9]
        # tmp = [3], [3, 15]
        # tmp = [20]
        # tmp = [7]
        return verticalTraversal

                
        
        