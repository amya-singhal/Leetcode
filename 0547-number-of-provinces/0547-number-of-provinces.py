class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1]*n
        
        def find(n1):
            a = n1
            while a != par[a]:
                par[n1] = par[par[n1]]
                a = par[n1]
            return a
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        ans = n
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if isConnected[i][j] == 1:
                    ans -= union(i, j)
        return ans