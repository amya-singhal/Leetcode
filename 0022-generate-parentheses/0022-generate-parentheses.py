class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """"
        n = 3
        tmp -> n*2 -> add it to the ans
        l and r
        l < n:
        add lP
        and whenever r < l:
         we can add rP
        """
        l = 0
        r = 0
        ansArray = []
        def dfs(l, r, tmp):
            if (len(tmp) == n*2):
                ansArray.append(tmp)
                return
            if (l < n):
                dfs(l+1, r, tmp+'(')
            if (r < l):
                dfs(l, r+1, tmp+')')
        dfs(0,0,"")
        return ansArray