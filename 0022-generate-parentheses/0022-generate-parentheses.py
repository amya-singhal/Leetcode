class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(tmp, l, r):
            if len(tmp) == n*2:
                ans.append(tmp)
                return
            if l < n:
                helper(tmp+"(", l+1, r)
            if r < l:
                helper(tmp+ ")", l, r+1)
        helper("", 0, 0)
        return ans