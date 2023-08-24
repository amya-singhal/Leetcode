class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def helper(s):
            if len(s) == 0:
                return 1
            if s in cache:
                return cache[s]
            if s[0] == '0':
                return 0
            if s[0] == '1' and len(s) > 1:
                cache[s] = helper(s[1:]) + helper(s[2:])
            elif s[0] == '2' and len(s) > 1 and s[1] != '7' and s[1] != '8' and s[1] != '9':
                    cache[s] = helper(s[1:]) + helper(s[2:])
            else:
                cache[s] = helper(s[1:])
            # print(cache)
            return cache[s]

        return helper(s)