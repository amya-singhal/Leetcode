# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        
        queue = [[root, 0, 0]]
        while queue:
            l = len(queue)
            for _ in range(l):
                q = queue.pop(0)
                element, x, y = q[0], q[1], q[2]
                if not element:
                    continue
                levels[y].append((x, element.val))
                if element.left:
                    queue.append([element.left, x+1, y-1])
                if element.right:
                    queue.append([element.right, x+1, y+1])
        # print(levels)
        ans = []
        minkey = min(levels.keys())
        i = minkey
        while i in levels:
            sorted_levels = sorted(levels[i])
            tmp = []
            for x, y in sorted_levels:
                tmp.append(y)
            ans.append(tmp)
            i += 1
        
        return ans
        