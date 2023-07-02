class Solution:
    def reverseWords(self, s: str) -> str:
        ansString = ""
        tmp = ""
        words = []
        for i in range(0, len(s)):
            if s[i] == ' ':
                if tmp != "":
                    words.append(tmp)
                    tmp = ""
                else:
                    continue
            else:
                tmp += s[i]
        if tmp != "":
            words.append(tmp)
        for word in words:
            ansString = ' ' + word + ansString
        return ansString[1:]
        