class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # tmp = ""
        # ans = []
        # helper function- base case, len(tmp) == len digits
        # dict = {}
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            return []
        strCombination = []
        def helper(digits, tmp):
            if len(digits) == 0:
                strCombination.append(tmp)
                tmp = ""
                return
            for s in d[digits[0]]:
                helper(digits[1:], tmp+s)
        helper(digits, "")
        return strCombination