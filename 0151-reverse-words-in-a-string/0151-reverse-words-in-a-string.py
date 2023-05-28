class Solution:
    def reverseWords(self, s: str) -> str:
        a = []
        tmp = ""
        for i in s:
            if (i == ' '):
                if (tmp != ""):
                    a.append(tmp)
                tmp = ""
            else:
                tmp += i
        if (tmp != ""):
            a.append(tmp)
        finalString = ""
        for i in reversed(range(1, len(a))):
            finalString += a[i] + " "
        finalString += a[0]
        return finalString