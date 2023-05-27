"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def dfs(node, visited):
            neigh = []
            newNode = Node(node.val)
            visited[node.val] = newNode
            for i in node.neighbors:
                if (i.val not in visited):
                    neigh.append(dfs(i, visited))
                else:
                    neigh.append(visited[i.val])
            newNode.neighbors = neigh
            return newNode
        return dfs(node, visited)
        