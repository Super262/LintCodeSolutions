def shortestPath2(grid: list) -> int:
    if not grid or grid[0][0] == 1:
        return -1
    directions = [(2, 1), (2, -1), (1, 2), (1, -2)]
    path_len = 0
    import collections
    q = collections.deque([(0, 0)])
    grid[0][0] = 1
    while q:
        path_len += 1
        for _ in range(len(q)):
            cur_y, cur_x = q.popleft()
            grid[cur_y][cur_x] = 1
            if cur_y == len(grid) - 1 and cur_x == len(grid[0]) - 1:
                return path_len
            for d in directions:
                next_y = cur_y + d[0]
                next_x = cur_x + d[1]
                if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x] != 1:
                    q.append((next_y, next_x))
                    grid[next_y][next_x] = 1
    return -1


if __name__ == '__main__':
    g = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print(shortestPath2(grid=g))
