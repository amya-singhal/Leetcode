class Solution:
    def partitionString(self, s: str) -> int:
        """
        s = "abacaba"
        tmp = (a)
        ans = 0, 1, 2, 3, 4
        """
        ans = 0
        tmp = set()
        for i in range(len(s)):
            if s[i] in tmp:
                ans += 1
                tmp = set()
            tmp.add(s[i])
        if tmp:
            ans += 1
        return ans