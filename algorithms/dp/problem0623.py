class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    class TrieNode:
        def __init__(self):
            self.is_word = False
            self.word_val = ""
            self.son = dict()

    def insert(self, root: TrieNode, word: str):
        for ch in word:
            if ch not in root.son:
                root.son[ch] = self.TrieNode()
            root = root.son[ch]
        root.is_word = True
        root.word_val = word

    def kDistance(self, words: list, target: str, k: int) -> list:
        trie_root = self.TrieNode()
        for w in words:
            self.insert(trie_root, w)
        f_current = [i for i in range(0, len(target) + 1)]
        results = []
        self.dfs(trie_root, target, f_current, k, results)
        return results

    def dfs(self, root: TrieNode, target: str, f_current: list, max_distance: int, results: list):
        if root.is_word and f_current[-1] <= max_distance:
            results.append(root.word_val)
        for ch in root.son:
            f_new = [0] * (len(target) + 1)
            f_new[0] = f_current[0] + 1  # 千万不要忘记这个初始化操作：递增1
            for l in range(1, len(target) + 1):
                if ch == target[l - 1]:
                    f_new[l] = min(f_new[l - 1] + 1, f_current[l] + 1, f_current[l - 1])
                else:
                    f_new[l] = min(f_new[l - 1], f_current[l], f_current[l - 1]) + 1
            self.dfs(root.son[ch], target, f_new, max_distance, results)
