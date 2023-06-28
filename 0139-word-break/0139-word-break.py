class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        array = [0]*(l+1)
        array[l] = 1
        for i in range(l-1, -1, -1):
            for word in wordDict:
                if ((i + len(word) <= l) and (s[i:i+len(word)] == word)):
                    array[i] = array[i + len(word)]
                if array[i] == 1:
                    break
        return array[0]