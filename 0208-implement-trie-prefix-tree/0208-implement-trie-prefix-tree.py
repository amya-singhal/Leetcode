class Trie:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def insert(self, word: str) -> None:
        c = self
        for w in word:
            if w not in c.children:
                c.children[w] = Trie()
            c = c.children[w]
        c.word = True

    def search(self, word: str) -> bool:
        c = self
        for w in word:
            if w not in c.children:
                return False
            c = c.children[w]
        return c.word

    def startsWith(self, prefix: str) -> bool:
        c = self
        for w in prefix:
            if w not in c.children:
                return False
            c = c.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)