class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        anti_diag = set()
        tmp = []
        ans = []
        def backtrack(r):
            nonlocal col, diag, anti_diag, tmp, ans
            if r == n:
                ans.append(tmp[:])
                return
            for c in range(n):
                if c in col or (r+c) in diag or (r-c) in anti_diag:
                    continue
                col.add(c)
                diag.add(r+c)
                anti_diag.add(r-c)
                tmp.append('.'*c + 'Q' + '.'*(n-c-1))
                
                backtrack(r+1)
                
                col.remove(c)
                diag.remove(r+c)
                anti_diag.remove(r-c)
                tmp.pop()
                
        backtrack(0)
        return ans