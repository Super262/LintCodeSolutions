class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words: list) -> str:
        # 计算入度时，重复的边只计算一次！
        if not words:
            return ""
        if len(words) == 1:
            return words[0]
        neighbors = {}
        in_degree = {}
        for w in words:
            for ch in w:
                neighbors[ch] = set()
                in_degree[ch] = 0
        for i in range(1, len(words)):
            variance_index = self.different_index(words[i - 1], words[i])
            if variance_index == -1:
                if len(words[i - 1]) > len(words[i]):
                    return ""
                continue
            if words[i][variance_index] not in neighbors[words[i - 1][variance_index]]:
                neighbors[words[i - 1][variance_index]].add(words[i][variance_index])
                in_degree[words[i][variance_index]] += 1
        queue = []
        for v in in_degree:
            if in_degree[v] == 0:
                queue.append(v)
        import heapq
        heapq.heapify(queue)
        order = []
        while queue:
            node = heapq.heappop(queue)
            order.append(node)
            for n in neighbors[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    heapq.heappush(queue, n)
        if len(order) == len(in_degree):
            return "".join(order)
        return ""

    def different_index(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return -1
        i = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                return i
            i += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["ac", "ab", "zc", "zb"]))
