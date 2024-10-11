class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        ans = 0
        middle = False
        visited = set()
        for word in words:
            # print(d, word, ans)
            if word[0] == word[1]:
                if d[word] > 1:
                    # print(d[word] // 2, d[word]%2)
                    ans += 4*(d[word] // 2)
                    d[word] = d[word]%2
                if not middle and d[word] > 0:
                    ans += 2
                    d[word] -= 1
                    middle = True
            elif d[word[::-1]] > 0 and d[word] > 0:
                ans += 4
                d[word] -= 1
                d[word[::-1]] -= 1
        
        return ans