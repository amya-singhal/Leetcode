class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 3
        ["((()))","(()())","(())()","()(())","()()()"]
        
        l,r =  2,1   2,1    3,0
        tmp= ["()(", "(()", "((("]
        l = r = n
        """
        ans = []
        def helper(l, r, tmp):
            if l == n and r == n:
                ans.append(tmp)
                return
            if l < n:
                helper(l+1, r, tmp+'(')
            if r < l:
                helper(l, r+1, tmp+")")
        helper(0,0,"")
        return ans
                
            