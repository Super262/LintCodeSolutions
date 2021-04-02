class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid: list) -> int:
        # 多源点bfs：从所有的源点出发，往外感染即可。
        visited = []
        for i in range(len(grid)):
            visited.append([False] * len(grid[0]))
        import collections
        queue = collections.deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    queue.append((y, x))
                    visited[y][x] = True
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        path_len = self.bfs(grid, queue, directions, visited)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0 and not visited[y][x]:
                    return -1
        return path_len

    def bfs(self, grid: list, queue, directions: tuple, visited: list) -> int:
        path_len = -1
        while queue:
            path_len += 1
            for _ in range(len(queue)):
                root = queue.popleft()
                for d in directions:
                    next_y = root[0] + d[0]
                    next_x = root[1] + d[1]
                    if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]) or visited[next_y][
                        next_x] or grid[next_y][next_x] == 2:
                        continue
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
        return path_len
