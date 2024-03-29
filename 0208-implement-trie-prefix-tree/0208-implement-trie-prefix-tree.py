class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr= self
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        if curr.isWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)