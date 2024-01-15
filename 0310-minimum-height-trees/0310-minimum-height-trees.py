class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # create graph
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # [[1], [0,2,3],[1],[1]]
        leaf_nodes = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf_nodes.append(i)
        while (n > 2):
            leaf_count = len(leaf_nodes)
            print(leaf_nodes, leaf_count)
            n -= leaf_count
            for i in range(leaf_count):
                leaf = leaf_nodes.pop(0)
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaf_nodes.append(neighbor)
        return leaf_nodes