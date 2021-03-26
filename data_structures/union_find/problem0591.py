class ConnectingGraph3:

    def __init__(self, n: int):
        self.father = {}
        self.size = n
        for i in range(1, n + 1):
            self.father[i] = i

    def connect(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a
            self.size -= 1
        self.find(a)
        self.find(b)

    def find(self, node: int) -> int:
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

    def query(self) -> int:
        return self.size
