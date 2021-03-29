class Trie:

    def __init__(self):
        self.sons = {}
        self.isWord = False
        self.word = ""

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word: str) -> None:
        p = self
        for ch in word:
            if ch not in p.sons:
                p.sons[ch] = Trie()
            p = p.sons[ch]
        p.isWord = True
        p.word = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word: str) -> bool:
        p = self
        for ch in word:
            if ch not in p.sons:
                return False
            p = p.sons[ch]
        return p.isWord and p.word == word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix: str) -> bool:
        p = self
        for ch in prefix:
            if ch not in p.sons:
                return False
            p = p.sons[ch]
        return True
