class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph: list) -> list:
        result = []
        in_degree = self.get_in_degree(graph)
        start_points = [v for v in in_degree if in_degree[v] == 0]
        import collections
        q = collections.deque(start_points)
        while q:
            node = q.popleft()
            result.append(node)
            for n in node.neighbors:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        return result

    def get_in_degree(self, graph: list) -> dict:
        in_degree = {x: 0 for x in graph}
        for node in graph:
            for n in node.neighbors:
                in_degree[n] += 1
        return in_degree
