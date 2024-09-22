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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        que = [root]
        prev = None
        while que:
            lenQ = len(que)
            for _ in range(lenQ):
                popped = que.pop(0)
                if not popped:
                    continue
                if prev:
                    prev.next = popped
                prev = popped
                if popped.left:
                    que.append(popped.left)
                if popped.right:
                    que.append(popped.right)    
            prev = None
        
        return root