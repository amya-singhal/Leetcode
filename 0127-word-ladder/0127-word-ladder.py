class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)
        
        q = [beginWord]
        answer = 1
        visited = set()
        while q:
            lenQ = len(q)
            for i in range(lenQ):
                x = q.pop(0)
                visited.add(x)
                if x == endWord:
                    return answer
                for i in range(len(x)):
                    pattern = x[:i] + '*' + x[i+1:]
                    values = patterns[pattern]
                    for word in values:
                        if word not in visited:
                            q.append(word)
            answer += 1
        return 0
        