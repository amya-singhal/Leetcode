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
        for i in reversed(range(0, len(words))):
            ansString += words[i]
            if i != 0:
                ansString += ' '
        return ansString
        