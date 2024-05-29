class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        ans = 0
        d = defaultdict(int)
        l = 0 
        for r in range(length):
            d[s[r]] += 1
            while d[s[r]] == 2:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans