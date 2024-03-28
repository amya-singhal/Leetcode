class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        n = len(digits)
        if n == 0:
            return ans
        def helper(index, tmp):
            if index >= n:
                ans.append(tmp)
                return
            s = phone[digits[index]]
            for i in s:
                helper(index+1, tmp+i)
        helper(0, "")
        return ans
            
        