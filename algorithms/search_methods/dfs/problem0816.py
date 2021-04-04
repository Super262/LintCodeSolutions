class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n: int, roads: list) -> int:
        import sys
        graph = self.make_graph(n, roads)
        state_size = 1 << n
        f = [[sys.maxsize] * (n + 1) for _ in range(state_size)]
        f[1][1] = 0
        for cur_state in range(state_size):
            for i in range(2, n + 1):   # 注意：i >= 2
                if cur_state & (1 << (i - 1)) == 0:
                    continue
                prev_state = cur_state ^ (1 << (i - 1))
                for j in range(1, n + 1):
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    f[cur_state][i] = min(f[cur_state][i], f[prev_state][j] + graph[j][i])
        return min(f[state_size - 1])

    def make_graph(self, n: int, roads: list) -> list:
        import sys
        graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
        for start, end, distance in roads:
            graph[start][end] = min(graph[start][end], distance)  # end -> start 和 start -> end 要设置为一样的长度
            graph[end][start] = min(graph[end][start], distance)
        return graph
