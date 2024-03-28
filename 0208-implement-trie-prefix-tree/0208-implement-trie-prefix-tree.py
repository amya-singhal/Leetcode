class Trie:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self.children
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr['*'] = ''
        
    def search(self, word: str) -> bool:
        curr = self.children
        for l in word:
            if l in curr:
                curr = curr[l]
            else:
                return False
        return '*' in curr
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.children
        for l in prefix:
            if l in curr:
                curr = curr[l]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)