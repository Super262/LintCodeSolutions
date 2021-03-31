class Solution:

    def ladderLength(self, start: str, end: str, dict: set) -> int:
        if not dict:
            return 0
        if end not in dict:
            dict.add(end)
        if start not in dict:
            dict.add(start)
        visited_nodes = set()
        import collections
        q = collections.deque([start])
        visited_nodes.add(start)
        path_len = 0
        while q:
            path_len += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == end:
                    return path_len
                for next_node in self.get_next_words(node):
                    if next_node not in visited_nodes and next_node in dict:
                        visited_nodes.add(next_node)
                        q.append(next_node)
        return 0

    def get_next_words(self, word: str) -> list:
        words = []
        dict = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for ch in dict:
                if word[i] == ch:
                    continue
                words.append(word[:i] + ch + word[i + 1:])
        return words
