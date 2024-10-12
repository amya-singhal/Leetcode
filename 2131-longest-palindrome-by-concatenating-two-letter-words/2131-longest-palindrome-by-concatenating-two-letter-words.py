class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        total = 0
        double = 0
        hasSingle = False
        visited = set()
        for word in d.keys():
            # print(word)
            if word[0] == word[1]:
                if d[word] % 2 == 1:
                    hasSingle = True
                total += (d[word] // 2)
                # print(total, word)
            else:
                rev = word[1]+word[0]
                if rev in d:
                    c_rev = d[rev]
                    double += min(d[word], c_rev)
        # print(total, double)
        total = (total + double // 2)*4
        if hasSingle:
            total += 2
        return total