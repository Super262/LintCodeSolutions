class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes: list):
        if not nodes:
            return None
        visited = {}
        results = []
        for node in nodes:
            if node in visited and visited[node]:
                continue
            self.bfs(node, visited, results)
        return results

    def bfs(self, node: UndirectedGraphNode, visited: dict, results: list) -> None:
        result = []
        visited[node] = True
        import collections
        q = collections.deque()
        q.append(node)
        while q:
            cur_node = q.popleft()
            result.append(cur_node.label)
            for n in cur_node.neighbors:
                if n in visited and visited[n]:
                    continue
                visited[n] = True
                q.append(n)
        result.sort()
        results.append(result)
