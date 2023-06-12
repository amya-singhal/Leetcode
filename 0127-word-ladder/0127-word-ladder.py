class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        l = len(beginWord)
        patterns = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if (pattern not in patterns):
                    patterns[pattern] = [word]
                else:
                    patterns[pattern].append(word)
        queue = [(beginWord, 1)]
        visited = [beginWord]
        if beginWord in wordList:
            ans = 1
        else:
            ans = 0
        while(queue):
            for w in range(len(queue)):
                x, y = queue.pop(0)
                if (x == endWord):
                    return y
                for i in range(len(x)):
                    pattern = x[:i] + "*" + x[i+1:]
                    for p in patterns[pattern]:
                        if p not in visited:
                            queue.append((p, y+1))
                            visited.append(p)
        return 0
                
        