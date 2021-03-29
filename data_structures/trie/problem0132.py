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
        if self.board[y][x] not in trie_root["children"]:
            return
        child_node = trie_root["children"][self.board[y][x]]
        if child_node["isWord"]:
            self.results.append(str(self.words[child_node["wordIndex"]]))
            child_node["isWord"] = False
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
                if ch not in cur_p["children"]:
                    cur_p["children"][ch] = self.get_new_node()
                cur_p = cur_p["children"][ch]
            cur_p["isWord"] = True
            cur_p["wordIndex"] = wi

    def get_new_node(self) -> dict:
        # 通过这个方法每次开辟新的内存保存节点信息
        return {"children": {}, "wordIndex": -1, "isWord": False}
