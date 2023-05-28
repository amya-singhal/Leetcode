class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s-> abcabcbb
        
        """
        ans = 0
        for i in range(0, len(s)):
            tmp = ""
            for j in range(i, len(s)):
                if (s[j] in tmp):
                    break
                tmp += s[j]
            if (len(tmp) > ans):
                ans = len(tmp)
        return ans
                
            