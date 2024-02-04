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
        visited = {}
        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            ans = Node(node.val)
            visited[node] = ans
            neighbors = []
            for neigh in node.neighbors:
                neighbors.append(dfs(neigh))
            ans.neighbors = neighbors
            return ans
        
        return dfs(node)
                
                