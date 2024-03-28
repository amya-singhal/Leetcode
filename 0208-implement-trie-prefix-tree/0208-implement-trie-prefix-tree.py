class Trie:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self
        for l in word:
            if l not in curr.children:
                curr.children[l] = Trie()
            curr = curr.children[l]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        curr = self
        for l in word:
            if l in curr.children:
                curr = curr.children[l]
            else:
                return False
        return curr.isWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for l in prefix:
            if l in curr.children:
                curr = curr.children[l]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)