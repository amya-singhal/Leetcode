class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def recur(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i,j)]
            match = (i < len(s)) and ((s[i] == p[j]) or (p[j] == '.'))
            if j+1 < len(p) and p[j+1] == '*':
                cache[(i, j)] = (match and recur(i+1, j)) or recur(i, j+2)
                return cache[(i,j)]
            else:
                cache[(i,j)] = match and recur(i+1, j+1)
                return cache[(i,j)]
            
        return recur(0,0)
        