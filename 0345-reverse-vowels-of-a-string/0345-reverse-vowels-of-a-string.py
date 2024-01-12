class Solution:
    def reverseVowels(self, s: str) -> str:
        l = ['a','e','i','o','u','A','E','I','O','U']
        d = []
        for i in range(0, len(s)):
            if s[i] in l:
                d.append(s[i])
        d.reverse()
        x = 0
        answer = ""
        for i in range(0, len(s)):
            if s[i] in l:
                answer += d[x]
                x += 1
            else:
                answer += s[i]
        return answer
        
        