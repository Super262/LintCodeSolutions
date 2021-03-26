class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def numIslands2(self, n: int, m: int, operators: list) -> list:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        matrix = []
        father = {}
        for _ in range(n):
            matrix.append([0] * m)
        result = []
        for p in operators:
            if matrix[p.x][p.y] == 1:
                result.append(result[-1])
                continue
            matrix[p.x][p.y] = 1
            father[(p.x, p.y)] = (p.x, p.y)
            temp = 1
            if len(result) > 0:
                temp += result[-1]
            for d in directions:
                if n > p.x + d[0] >= 0 and 0 <= p.y + d[1] < m and matrix[p.x + d[0]][p.y + d[1]] == 1:
                    root_a = self.find(father, (p.x, p.y))
                    root_b = self.find(father, (p.x + d[0], p.y + d[1]))
                    if root_b != root_a:
                        self.connect(father, root_a, root_b)
                        temp -= 1
            result.append(temp)
        return result

    def connect(self, father: dict, a: tuple, b: tuple) -> None:
        father[b] = a
        self.find(father, a)
        self.find(father, b)

    def find(self, father: dict, node: tuple) -> tuple:
        path = []
        while father[node] != node:
            path.append(node)
            node = father[node]
        for n in path:
            father[n] = node
        return node
