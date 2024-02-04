"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {node.val : Node(node.val)}
        s = [node]
        
        while len(s) > 0:
            element = s.pop()
            curr = visited[element.val]
            neighbors = []
            for neigh in element.neighbors:
                if neigh.val not in visited:
                    visited[neigh.val] = Node(neigh.val)
                    s.append(neigh)
                neighbors.append(visited[neigh.val])
            curr.neighbors = neighbors
        return visited[node.val]
                
                