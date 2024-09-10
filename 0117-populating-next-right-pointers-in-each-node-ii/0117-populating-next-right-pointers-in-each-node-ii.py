"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levels = []
        s = [root]
        while s:
            l = len(s)
            level = []
            for _ in range(l):
                x = s.pop(0)
                if not x:
                    continue
                level.append(x)
                s.append(x.left)
                s.append(x.right)
            # print(level[0].val)
            levels.append(level)
        # print(levels)
        for level in levels:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            
        return root