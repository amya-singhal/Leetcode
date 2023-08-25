class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        patterns = defaultdict(list)
        n = len(wordList)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i]+"*"+word[i+1:]
                patterns[tmp].append(word)
        # print(patterns)
        queue = [(beginWord, 1)]
        visited = [beginWord]
        while queue:
            for w in range(len(queue)):
                x,y = queue.pop(0)
                if x == endWord:
                    return y
                for i in range(len(x)):
                    pattern = x[:i]+"*"+x[i+1:]
                    for word in patterns[pattern]:
                        if word not in visited:
                            queue.append((word, y+1))
                            visited.append(word)   
        return 0
                
        