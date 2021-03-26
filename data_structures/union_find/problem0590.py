class ConnectingGraph2:

    def __init__(self, n: int):
        self.father = {}
        self.size = {}
        for i in range(1, n + 1):
            self.father[i] = i
            self.size[i] = 1

    def connect(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_b != root_a:
            self.size[root_a] += self.size[root_b]
            self.father[root_b] = root_a
        root_a = self.find(a)
        root_b = self.find(b)

    def query(self, a: int) -> int:
        return self.size[self.find(a)]

    def find(self, node: int) -> int:
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node
