import collections


class Solution:

    # 双向BFS

    def shortestPath2(self, grid: list) -> int:
        if not grid or not grid[0]:
            return -1
        destination = (len(grid) - 1, len(grid[0]) - 1)
        source = (0, 0)
        # 这是双向BFS无法处理的特殊情况，需要单独应对！
        if destination == source:
            return 0
        forward_visited = set()
        backward_visited = set()
        if not self.node_valid(source[0], source[1], grid, forward_visited):
            return -1
        if not self.node_valid(destination[0], destination[1], grid, backward_visited):
            return -1
        forward_directions = ((1, 2), (-1, 2), (2, 1), (-2, 1))
        backward_directions = ((-1, -2), (1, -2), (-2, -1), (2, -1))
        distance = 0
        import collections
        forward_queue = collections.deque([source])
        backward_queue = collections.deque([destination])
        forward_visited.add(source)  # 不要忘记设置初始节点被访问过
        backward_visited.add(destination)  # 不要忘记设置初始节点被访问过
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(forward_queue, grid, forward_directions, forward_visited, backward_visited):
                return distance
            distance += 1
            if self.extend_queue(backward_queue, grid, backward_directions, backward_visited, forward_visited):
                return distance
        return -1

    def extend_queue(self, queue: collections.deque, grid: list, directions: tuple, current_visited: set,
                     opposite_visited: set) -> bool:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if not self.node_valid(new_x, new_y, grid, current_visited):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                current_visited.add((new_x, new_y))
        return False

    def node_valid(self, x: int, y: int, grid: list, visited: set) -> bool:
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        return (x, y) not in visited
