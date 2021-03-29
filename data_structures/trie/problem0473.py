class WordDictionary:

    def __init__(self):
        self.sons = {}
        self.is_word = False
        self.word = ""

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word: str) -> None:
        p = self
        for ch in word:
            if ch not in p.sons:
                p.sons[ch] = WordDictionary()
            p = p.sons[ch]
        p.is_word = True
        p.word = word

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word: str) -> bool:
        return self.find(word, 0, len(word) - 1)

    def find(self, word: str, start_index: int, end_index: int) -> bool:
        if start_index == end_index:
            if word[start_index] == ".":
                for ch in self.sons:
                    if self.sons[ch].is_word:
                        return True
            else:
                return word[start_index] in self.sons and self.sons[word[start_index]].is_word
        else:
            if word[start_index] == ".":
                for ch in self.sons:
                    if self.sons[ch].find(word, start_index + 1, end_index):
                        return True
            else:
                if word[start_index] not in self.sons:
                    return False
                return self.sons[word[start_index]].find(word, start_index + 1, end_index)
        return False
