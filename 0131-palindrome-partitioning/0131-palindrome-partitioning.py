class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def checkPalindrome(s):
            l = 0
            r = len(s)-1
            while (l < r):
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def helper(st, tmp):
            if len(st) == 0:
                ans.append(tmp[:])
                return
            for i in range(len(st)):
                if checkPalindrome(st[:i+1]):
                    helper(st[i+1:], tmp+[st[:i+1]])
        helper(s, [])
        return ans