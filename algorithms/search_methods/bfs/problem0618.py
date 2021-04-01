class UndirectedGraphNode:
    def __init__(self, x: int) -> None:
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph: list, values: dict, node: UndirectedGraphNode, target: int):
        if not graph or not values or not node:
            return None
        import collections
        queue = collections.deque([node])
        visited = {node: True}
        while queue:
            cur_size = len(queue)
            for _ in range(cur_size):
                cur_node = queue.popleft()
                if values[cur_node] == target:
                    return cur_node
                for n in cur_node.neighbors:
                    if n in visited and visited[n]:
                        continue
                    visited[n] = True
                    queue.append(n)
        return None
