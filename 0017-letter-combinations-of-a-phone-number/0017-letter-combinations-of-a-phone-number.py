class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        23
        2 -> a,b,c
        3 -> d,e,f
        bf: n^2
        
        
        """
        ans = []
        d = {'2' : 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8': 'tuv', '9':'wxyz'}
        if (len(digits) == 0):
            return []
        def helper(tmp, digits):
            if (len(digits) == 0):
                ans.append(tmp)
                return
            else:
                for x in d[digits[0]]:
                    helper(tmp +x, digits[1:])
        
        helper("", digits)
        return ans