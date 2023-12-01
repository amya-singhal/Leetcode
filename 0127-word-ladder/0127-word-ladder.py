class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        wordDic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # pattern
                p = word[:i] + "*" + word[i+1:]
                wordDic[p].append(word)
        visited = [beginWord]
        queue = [(beginWord, 1)]
        count = float(inf)
        while(queue):
            for w in range(len(queue)):
                (word, index) = queue.pop(0)
                if word == endWord:
                    count = min(count, index)
                for i in range(len(word)):
                    p = word[:i] + "*" + word[i+1:]
                    for nextWord in wordDic[p]:
                        if nextWord not in visited:
                            queue.append((nextWord, index+1))
                            visited.append(nextWord)
        if count == float(inf):
            return 0
        else:
            return count
        