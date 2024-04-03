class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def helper(s, tmp, count):
            if len(s) == 0:
                if count == 4:
                    l = len(tmp)
                    ans.append(tmp[:l-1])
                return
            for i in range(len(s)):
                integer = int(s[:i+1])
                if s[0] == '0' and len(s[:i+1]) > 1:
                    continue
                if integer <= 255 and integer >= 0 :
                    helper(s[i+1:], tmp+s[:i+1]+'.', count+1)
        helper(s, "", 0)
        return ans