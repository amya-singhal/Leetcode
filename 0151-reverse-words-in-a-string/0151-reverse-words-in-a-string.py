class Solution:
    def reverseWords(self, s: str) -> str:
        ansString = ""
        a = []
        tmp = ""
        for i in range(0, len(s)):
            if s[i] == ' ':
                if tmp != "":
                    a.append(tmp)
                tmp = ""
            else:
                tmp += s[i]
        if len(tmp):
            a.append(tmp)
        for i in reversed(range(0, len(a))):
            ansString = ansString + a[i]
            if i != 0:
                ansString = ansString + ' '                
        return ansString
            
        