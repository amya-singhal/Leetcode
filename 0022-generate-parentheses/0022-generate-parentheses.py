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
            if r == 0 and l == 0:
                ans.append(tmp)
                return
            elif r < 0 or l < 0 or r < l:
                return
            else:
                helper(l-1,r,tmp+'(')
                helper(l,r-1,tmp+')')
        helper(n,n,"")
        return ans
            
        