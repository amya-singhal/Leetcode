class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = {}
        
    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] =TrieNode()
            cur = cur.children[w]
        cur.isWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        n = len(board)
        m = len(board[0])
        ans, visit = set(), set()
        def dfs(i, j, node, word):
            if i<0 or j<0 or i==n or j==m or (i, j) in visit or board[i][j] not in node.children:
                return
            visit.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                ans.add(word)
            dfs(i+1, j, node, word)
            dfs(i-1, j, node, word)
            dfs(i, j+1, node, word)
            dfs(i, j-1, node, word)
            visit.remove((i, j))
        for i in range(n):
            for j in range(m):
                dfs(i, j, root, "")
        return list(ans)
        