# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # array = [] # index, level, value of node
        array = defaultdict(list)
        def bfs(root, level, index):
            if not root:
                return
            array[index].append([root.val, level])
            bfs(root.left, level+1, index-1)
            bfs(root.right, level+1, index+1)
        bfs(root, 0, 0)
        verticalTraversal = []
        for i in sorted(array.keys()):
            l = array[i]
            l.sort(key=lambda x:(x[1], x[0]))
            tmp = []
            for element in l:
                tmp.append(element[0])
            verticalTraversal.append(tmp)
        return verticalTraversal

                
        
        