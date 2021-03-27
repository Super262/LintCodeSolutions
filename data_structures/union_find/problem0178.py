class Solution:

    def validTree(self, n: int, edges: list) -> bool:
        if len(edges) != n - 1:
            return False
        father = [0] * n
        for v in range(n):
            father[v] = v
        count = n
        for e in edges:
            a_index = self.find_compress(father, e[0])
            b_index = self.find_compress(father, e[1])
            if a_index == b_index:
                continue
            father[b_index] = a_index
            count -= 1
        return count == 1

    def find_compress(self, father: list, a_index: int) -> int:
        path = []
        while father[a_index] != a_index:
            path.append(a_index)
            a_index = father[a_index]
        for node in path:
            father[node] = a_index
        return a_index
