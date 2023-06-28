class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        array = [0]*(l+1)
        array[0] = 1
        for i in range(0, l):
            if array[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        array[i+len(word)] = 1
        return array[-1]