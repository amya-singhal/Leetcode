class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        
        queue = [(beginWord,1)]
        
        while queue:
            curr, count = queue.pop(0)
            if curr == endWord:
                return count
            for i in range(len(curr)):
                for c in ascii_lowercase:
                    x = curr[:i] + c + curr[i+1:]
                    if x in wordList:
                        queue.append((x, count+1))
                        wordList.remove(x)
        
        return 0