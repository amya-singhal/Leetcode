class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "babad"
        # array = ['b', 'bab', 'aba', 'a', 'd']
        # s = "cbbd"
        # array = ['bb', 'c','b', 'b', 'd']
        ans = ""
        for i in range(len(s)):
            l, r = i-1, i+1
            tmp = s[i]
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                tmp = s[l]+tmp+s[r]
                l -= 1
                r += 1
            if len(ans) < len(tmp):
                ans = tmp
        for i in range(len(s)-1):
            l, r = i, i+1
            tmp = ""
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                tmp = s[l]+tmp+s[r]
                l -= 1
                r += 1
            if len(ans) < len(tmp):
                ans = tmp
        return ans
                