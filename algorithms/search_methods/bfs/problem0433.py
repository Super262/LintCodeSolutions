class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid: list) -> int:

        #   Using DFS may make the stack overflow!

        if not grid or not grid[0]:
            return 0
        h = len(grid)
        w = len(grid[0])
        visited = []
        for i in range(h):
            visited.append([False] * w)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        connected_count = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1 and not visited[y][x]:
                    self.bfs(grid, visited, directions, y, x, h, w)
                    connected_count += 1
        return connected_count

    def bfs(self, grid: list, visited: list, directions: list, start_y: int, start_x: int, h_max: int,
            w_max: int) -> None:
        import collections
        q = collections.deque()
        q.append((start_y, start_x))
        visited[start_y][start_x] = True
        while len(q) > 0:
            cur_size = len(q)
            for _ in range(cur_size):
                start_y, start_x = q.popleft()
                for o_y, o_x in directions:
                    next_y = start_y + o_y
                    next_x = start_x + o_x
                    if next_y >= h_max or next_y < 0 or next_x >= w_max or next_x < 0 or grid[next_y][next_x] == 0 or \
                            visited[next_y][next_x]:
                        continue
                    q.append((next_y, next_x))
                    visited[next_y][next_x] = True
