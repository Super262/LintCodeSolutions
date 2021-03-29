class Solution:
    # https://leetcode-cn.com/problems/word-squares/solution/dan-ci-fang-kuai-by-leetcode/

    def wordSquares(self, words: list) -> list:
        if not words:
            return []
        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)
        results = []
        for w in self.words:
            self.backtracking(1, [w], results)
        return results

    def buildTrie(self, words) -> None:
        self.trie = {"#": []}
        for wi in range(len(words)):
            p = self.trie
            p["#"].append(wi)
            for ch in words[wi]:
                if ch not in p:
                    p[ch] = {"#": []}
                p = p[ch]
                p["#"].append(wi)

    def backtracking(self, step, word_squares_temp: list, results: list) -> None:
        if step == self.N:
            results.append(word_squares_temp[:])
            return
        prefix = "".join([w[step] for w in word_squares_temp])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares_temp.append(candidate)
            self.backtracking(step + 1, word_squares_temp, results)
            word_squares_temp.pop()

    def getWordsWithPrefix(self, prefix: str) -> list:
        p = self.trie
        for ch in prefix:
            if ch not in p:
                return []
            p = p[ch]
        return [self.words[i] for i in p["#"]]
