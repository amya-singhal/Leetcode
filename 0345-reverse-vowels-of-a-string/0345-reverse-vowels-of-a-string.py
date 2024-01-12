class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        l = 0
        r = length-1
        d = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        while (l < r):
            if s[l] in d and s[r] in d:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in d:
                r -= 1
            else:
                l += 1
        return ''.join(s)