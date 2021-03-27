class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def numIslands2(self, n: int, m: int, operators: list) -> list:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        matrix = [0] * (n * m)
        father = [i for i in range(n * m)]
        result = []
        for p in operators:
            if matrix[self.point_to_int(p.x, p.y, m)] == 1:
                result.append(result[-1])
                continue
            matrix[self.point_to_int(p.x, p.y, m)] = 1
            father[self.point_to_int(p.x, p.y, m)] = self.point_to_int(p.x, p.y, m)
            temp = 1
            if len(result) > 0:
                temp += result[-1]
            for d in directions:
                next_x = p.x + d[0]
                next_y = p.y + d[1]
                if n > next_x >= 0 and 0 <= next_y < m and matrix[self.point_to_int(next_x, next_y, m)] == 1:
                    root_a = self.find(father, self.point_to_int(p.x, p.y, m))
                    root_b = self.find(father, self.point_to_int(next_x, next_y, m))
                    if root_b != root_a:
                        self.connect(father, root_a, root_b)
                        temp -= 1
            result.append(temp)
        return result

    def connect(self, father: list, a_index: int, b_index: int) -> None:
        father[b_index] = a_index
        self.find(father, b_index)

    def find(self, father: list, nodeIndex: int) -> int:
        path = []
        while father[nodeIndex] != nodeIndex:
            path.append(nodeIndex)
            nodeIndex = father[nodeIndex]
        for n in path:
            father[n] = nodeIndex
        return nodeIndex

    def point_to_int(self, x: int, y: int, m: int) -> int:
        return x * m + y
