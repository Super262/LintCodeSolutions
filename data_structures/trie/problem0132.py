class Solution:

    def __init__(self):
        self.trie_root = None
        self.results = []
        self.board = None
        self.words = None
        self.H = -1
        self.W = -1
        self.directions = []

    def wordSearchII(self, board: list, words: list) -> list:
        if not board or not words:
            return self.results
        self.board = board
        self.words = words
        self.H = len(self.board)
        self.W = len(self.board[0])
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.build_trie()
        for y in range(self.H):
            for x in range(self.W):
                self.search(self.trie_root, y, x)
        return self.results

    def search(self, trie_root: dict, y: int, x: int) -> None:
        ch_ord = ord(self.board[y][x]) - ord('a')
        if ch_ord not in trie_root[26]:
            return
        child_node = trie_root[26][ch_ord]
        if child_node[27]:
            self.results.append(self.words[child_node[28]])
            child_node[27] = False
        prev_val = self.board[y][x]
        self.board[y][x] = "#"
        for d in self.directions:
            next_y = y + d[0]
            next_x = x + d[1]
            if next_y >= self.H or next_y < 0 or next_x >= self.W or next_x < 0 or self.board[next_y][next_x] == "#":
                continue
            self.search(child_node, next_y, next_x)
        self.board[y][x] = prev_val

    def build_trie(self) -> None:
        self.trie_root = self.get_new_node()
        for wi in range(len(self.words)):
            cur_p = self.trie_root
            for ch in self.words[wi]:
                ch_ord = ord(ch) - ord('a')
                if ch_ord not in cur_p[26]:
                    cur_p[26][ch_ord] = self.get_new_node()
                cur_p = cur_p[26][ch_ord]
            cur_p[27] = True
            cur_p[28] = wi

    def get_new_node(self) -> dict:
        # 通过这个方法每次开辟新的内存保存节点信息
        return {26: {}, 27: False, 28: -1}
