class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        "abcadef"
        {'a':0, 'b':1, 'c':2}
        "abba"
        {'a':0, 'b':2}
        "pwwkew"
        """
        d = defaultdict(int)
        tmp = 0 
        ans = 0
        for i in range(len(s)):
            if s[i] in d:
                tmp = max(tmp, d[s[i]]+1)
            ans = max(ans, i-tmp+1)
            d[s[i]] = i
        return ans
                
                
                
                