class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
        #print(graph)
        visited = set()
        ans = []
        
        def dfs(email, res):
            nonlocal graph, visited
            visited.add(email)
            for n in graph[email]:
                if n not in visited:
                    dfs(n, res)
            res.append(email)
            return res
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visited:
                    res = dfs(email, [])
                    ans.append([name] + sorted(res))
        return ans