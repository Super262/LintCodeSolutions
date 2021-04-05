class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    class Trie:
        def __init__(self):
            self.is_word = False
            self.word_value = ""
            self.children = {}

    def wordSearchII(self, board: list, words: list) -> list:
        root = self.build_trie(words)
        results = []
        visited = []
        for _ in range(len(board)):
            visited.append([False] * len(board[0]))
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for y in range(len(board)):
            for x in range(len(board[0])):
                ch_ord = ord(board[y][x]) - ord("a")
                if ch_ord not in root.children:
                    continue
                visited[y][x] = True
                self.dfs_get_results_and_prune(root.children[ch_ord], board, visited, y, x, directions, results)
                visited[y][x] = False
        return results

    def dfs_get_results_and_prune(self, root: Trie, board: list, visited: list, start_y: int, start_x: int,
                                  directions: tuple, results: list) -> bool:
        # 找到单词并删除叶节点，提速20倍！
        if root.is_word:
            results.append(root.word_value)
            root.is_word = False
            if not root.children:
                return True
        for d in directions:
            next_y = start_y + d[0]
            next_x = start_x + d[1]
            if next_y < 0 or next_y >= len(board) or next_x < 0 or next_x >= len(board[0]) or visited[next_y][next_x]:
                continue
            ch_ord = ord(board[next_y][next_x]) - ord("a")
            if ch_ord not in root.children:
                continue
            visited[next_y][next_x] = True
            if self.dfs_get_results_and_prune(root.children[ch_ord], board, visited, next_y, next_x, directions,
                                              results):
                root.children.pop(ch_ord)
            visited[next_y][next_x] = False
        return len(root.children) == 0

    def build_trie(self, words: list) -> Trie:
        root = self.Trie()
        if not words:
            return root
        for w in words:
            self.add_word(root, w)
        return root

    def add_word(self, root: Trie, word: str) -> None:
        if not root or not word:
            return
        cur_node = root
        for ch in word:
            ch_ord = ord(ch) - ord("a")
            if ch_ord not in cur_node.children:
                cur_node.children[ch_ord] = self.Trie()
            cur_node = cur_node.children[ch_ord]
        cur_node.is_word = True
        cur_node.word_value = word
