class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    import collections

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    # 双向BFS
    def shortestPath(self, grid: list, source: Point, destination: Point) -> int:
        if not grid or not grid[0]:
            return -1
        forward_visited = set()
        backward_visited = set()
        if not self.node_valid(grid, forward_visited, source.x, source.y):
            return -1
        if not self.node_valid(grid, backward_visited, destination.x, destination.y):
            return -1
        # 这是双向BFS无法处理的特殊情况，需要单独应对！
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        directions = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        forward_queue = self.collections.deque([(source.x, source.y)])
        backward_queue = self.collections.deque([(destination.x, destination.y)])
        forward_visited.add((source.x, source.y))  # 不要忘记设置初始节点被访问过
        backward_visited.add((destination.x, destination.y))  # 不要忘记设置初始节点被访问过
        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(forward_queue, grid, directions, forward_visited, backward_visited):
                return distance
            distance += 1  # 不要忘记这一句！
            if self.extend_queue(backward_queue, grid, directions, backward_visited, forward_visited):
                return distance
        return -1

    def extend_queue(self, queue: collections.deque, grid: list, directions: tuple, current_visited: set,
                     opposite_visited: set) -> bool:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if not self.node_valid(grid, current_visited, new_x, new_y):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                current_visited.add((new_x, new_y))
        return False

    def node_valid(self, grid: list, visited: set, x: int, y: int) -> bool:
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        return (x, y) not in visited
