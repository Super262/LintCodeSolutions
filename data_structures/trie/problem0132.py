class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board: list, words: list) -> list:
        results = []
        if not board or not words:
            return results
        trie_root = self.build_trie(words)
        for y in range(len(board)):
            for x in range(len(board[y])):
                self.search(trie_root, board, y, x, words, results)
        return results

    def search(self, trie_root: dict, board: list, y: int, x: int, words: list, results: list) -> None:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        if board[y][x] not in trie_root["children"]:
            return
        child_node = trie_root["children"][board[y][x]]
        if child_node["isWord"]:
            results.append(str(words[child_node["wordIndex"]]))
            child_node["isWord"] = False
        prev_val = board[y][x]
        board[y][x] = "#"
        for d in directions:
            next_y = y + d[0]
            next_x = x + d[1]
            if next_y >= len(board) or next_y < 0 or next_x >= len(board[next_y]) or next_x < 0 or board[next_y][
                next_x] == "#":
                continue
            self.search(child_node, board, next_y, next_x, words, results)
        board[y][x] = prev_val

    def build_trie(self, words: list) -> dict:
        trie_root = self.get_new_node()
        for wi in range(len(words)):
            cur_p = trie_root
            for ch in words[wi]:
                if ch not in cur_p["children"]:
                    cur_p["children"][ch] = self.get_new_node()
                cur_p = cur_p["children"][ch]
            cur_p["isWord"] = True
            cur_p["wordIndex"] = wi
        return trie_root

    def get_new_node(self) -> dict:
        # 通过这个方法每次开辟新的内存保存节点信息
        return {"children": {}, "wordIndex": -1, "isWord": False}
