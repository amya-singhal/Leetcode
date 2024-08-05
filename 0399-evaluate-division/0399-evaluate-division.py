class Solution:
    
    def parseEquations(self, equations: List[List[str]], values: List[float]):
        graph = defaultdict(list)
        for i in range(len(equations)):
            numerator, denominator = equations[i][0], equations[i][1]
            value = values[i]
            graph[numerator].append((denominator, value))
            reverse_value = 1/ value
            graph[denominator].append((numerator, reverse_value))
        return graph
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.parseEquations(equations, values)
        # print(graph)
        
        def dfs(numerator, denominator):
            visited = set()
            queue = [(numerator, 1)]
            while queue:
                num, value = queue.pop(0)
                if num == denominator:
                    return value
                visited.add(num)
                for neigh, neighVal in graph[num]:
                    if neigh not in visited:
                        queue.append((neigh, value*neighVal))
            return -1
                    
            
        queryValues = []
        for query in queries:
            # print(queryValues)
            qNum, qDen = query[0], query[1]
            if qNum not in graph or qDen not in graph:
                queryValues.append(-1)
                continue
            if qNum == qDen:
                queryValues.append(1)
                continue
            queryValues.append(dfs(qNum, qDen))
        return queryValues
        