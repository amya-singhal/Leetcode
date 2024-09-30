class Trie():
    def __init__(self):
        self.children = {}
        self.word = False
    
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.word = True
        
    def search_word(self, word):
        # print(word)
        curr = self
        def recurse(word, curr):
            if not word:
                return curr.word
            char = word[0]
            ans = False
            if char == '.':
                # print("here1")
                for child in curr.children:
                    ans = ans or recurse(word[1:], curr.children[child])
            elif char in curr.children:
                # print("here2")
                ans = recurse(word[1:], curr.children[char])
            else:
                return False
            
            return ans
        return recurse(word, curr)
        
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add_word(word)

    def search(self, word: str) -> bool:
        return self.trie.search_word(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)