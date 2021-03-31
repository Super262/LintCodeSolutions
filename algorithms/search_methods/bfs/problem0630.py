class Solution:

    def shortestPath2(self, grid: list) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        directions = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        path_len = -1
        import collections
        q = collections.deque([(0, 0)])
        grid[0][0] = 1
        while q:
            path_len += 1
            for _ in range(len(q)):
                cur_x, cur_y = q.popleft()
                grid[cur_x][cur_y] = 1
                if cur_y == len(grid[0]) - 1 and cur_x == len(grid) - 1:
                    return path_len
                for d in directions:
                    next_x = cur_x + d[0]
                    next_y = cur_y + d[1]
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] != 1:
                        q.append((next_x, next_y))
                        grid[next_x][next_y] = 1
        return -1
