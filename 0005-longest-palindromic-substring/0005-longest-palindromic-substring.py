class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalin = ""
        # odd len
        for i in range(0, len(s)):
            l, r = i-1, i+1
            temp = s[i]
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                temp = s[l] + temp + s[r]
                l -= 1
                r += 1
            if len(temp) > len(longestPalin):
                longestPalin = temp
        # even len
        for i in range(0, len(s)-1):
            l, r = i, i+1
            temp = ""
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                temp = s[l] + temp + s[r]
                l -= 1
                r += 1
            if len(temp) > len(longestPalin):
                longestPalin = temp
        return longestPalin
        