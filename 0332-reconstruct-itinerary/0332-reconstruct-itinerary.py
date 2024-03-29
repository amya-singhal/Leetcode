class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjLst = defaultdict(list)
        for x, y in tickets:
            adjLst[x].append(y)
        for src in adjLst.keys():
            adjLst[src].sort()
        # print(adjLst)   
        path = []
        def dfs(src):
            while adjLst[src]:
                x = adjLst[src].pop(0)
                # print("x", x)
                dfs(x)
            path.append(src)
            # print(path)
        dfs("JFK")
        return path[::-1]

        