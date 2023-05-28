class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(tmp, l, r):
            if (len(tmp) == n*2):
                ans.append(tmp)
                return
            if (l < n):
                dfs(tmp + '(', l+1, r)
            if (r < l):
                dfs(tmp + ')', l, r+1)
            
        dfs('', 0, 0)
        return ans