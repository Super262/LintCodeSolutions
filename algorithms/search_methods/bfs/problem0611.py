class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid: list, source: Point, destination: Point) -> int:
        if not grid:
            return -1
        h_max = len(grid)
        w_max = len(grid[0])
        if source.x >= h_max or source.x < 0 or source.y < 0 or source.y >= w_max or grid[source.x][
            source.y] == 1:
            return -1
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        visited = []
        for _ in range(h_max):
            visited.append([False] * w_max)
        import collections
        q = collections.deque()
        q.append((source.x, source.y))
        path_len = -1
        while len(q) > 0:
            path_len += 1
            current_size = len(q)
            for _ in range(current_size):
                node = q.popleft()
                if node[0] == destination.x and node[1] == destination.y and grid[node[0]][node[1]] == 0:
                    return path_len
                for d in directions:
                    next_x = node[0] + d[0]
                    next_y = node[1] + d[1]
                    if next_x < 0 or next_x >= h_max or next_y < 0 or next_y >= w_max or grid[next_x][next_y] == 1 or \
                            visited[next_x][next_y]:
                        continue
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True
        return -1
