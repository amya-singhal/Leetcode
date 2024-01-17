class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        # dict : ['pattern': 'corresponding words']
        patterndict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                patterndict[pattern].append(word)
        # patterndict = ['*it':['hit'], 'h*t':['hit','hot']....]
        que = [beginWord] # [dog, log]
        visited = [beginWord] # [hit, hot, dot, lot, dog, log]
        answer = 1 # 2,3,4
        while que:
            for _ in range(len(que)):
                x = que.pop(0) # [hit]
                if str(x) == endWord:
                    return answer
                for i in range(len(x)):
                    pattern = x[:i]+'*'+x[i+1:] # *it, h*t
                    values = patterndict[pattern]
                    for y in values:
                        if y not in visited:
                            visited.append(y)
                            que.append(y)
            answer += 1
        return 0