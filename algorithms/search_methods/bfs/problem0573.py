class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    # 乍一看像598 zombie那题 只不过只有一个zombie即post office 但此题难点在于需要逆向考虑
    # 逆向思维从house开始BFS 否则从empty开始会TLE 还是有点费脑子的
    # 这个题告诉我们 当TLE时候 去集合中找找其他部分数量少的 来进行操作 尤其对这种单一操作BFS时间消耗大的题目
    def shortestDistance(self, grid: list) -> int:
        if not grid or not grid[0]:
            return -1
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        houses_count = []
        distance = []
        visited = []
        houses_nums = 0
        for y in range(len(grid)):
            distance.append([0] * len(grid[0]))
            houses_count.append([0] * len(grid[0]))
            visited.append([False] * len(grid[0]))
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    houses_nums += 1
        import sys
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 1:
                    continue
                self.bfs(grid, y, x, directions, houses_count, distance, sys.maxsize)
        min_path_len = sys.maxsize
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if houses_count[y][x] != houses_nums:
                    continue
                min_path_len = min(min_path_len, distance[y][x])
        if min_path_len == sys.maxsize:
            return -1
        return min_path_len

    def bfs(self, grid: list, start_y: int, start_x: int, directions: tuple, houses_count: list, distance: list,
            maxsize: int) -> None:
        visited = []
        for _ in range(len(grid)):
            visited.append([False] * len(grid[0]))
        import collections
        queue = collections.deque([(start_y, start_x)])
        visited[start_y][start_x] = True
        path_len = 0
        while queue:
            for _ in range(len(queue)):
                root = queue.popleft()
                if distance[root[0]][root[1]] == maxsize:
                    distance[root[0]][root[1]] = 0
                distance[root[0]][root[1]] += path_len
                for d in directions:
                    next_y = d[0] + root[0]
                    next_x = d[1] + root[1]
                    if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]) or grid[next_y][
                        next_x] == 2 or grid[next_y][next_x] == 1 or visited[next_y][next_x]:
                        continue
                    queue.append((next_y, next_x))
                    houses_count[next_y][next_x] += 1
                    visited[next_y][next_x] = True
            path_len += 1
