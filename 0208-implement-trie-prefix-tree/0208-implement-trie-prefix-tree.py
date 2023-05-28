class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        x = self.root
        for c in word:
            if c not in x.children:
                x.children[c] = Node()
            x = x.children[c]
        x.end = True

    def search(self, word: str) -> bool:
        x = self.root
        for i in word:
            if i not in x.children:
                return False
            x = x.children[i]
        if (x.end == True):
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        x = self.root
        for i in prefix:
            if i not in x.children:
                return False
            x = x.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)