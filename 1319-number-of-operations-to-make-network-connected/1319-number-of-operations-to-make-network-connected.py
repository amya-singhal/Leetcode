class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        3 3
        """
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        # print(graph)
        def searchCom(num, visited):
            edges = 0
            stack = [num]
            while stack:
                popped = stack.pop()
                edges += len(graph[popped])
                for neigh in graph[popped]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
            return edges
            
        visited = set()
        numExtraEdges = 0
        numComponents = 0
        for i in range(n):
            if i not in visited:
                prev = len(visited)
                visited.add(i)
                edges = searchCom(i, visited)
                numComputers = len(visited) - prev
                numEdges = edges // 2
                numExtraEdges += numEdges - (numComputers-1)
                numComponents += 1
                
        # print(numComponents, numExtraEdges)
        if (numComponents-1) <= numExtraEdges:
            return numComponents-1
        return -1
                
        
            