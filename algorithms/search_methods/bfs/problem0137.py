class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return node
        visited_copy = {}
        import collections
        q = collections.deque()
        q.append(node)
        visited_copy[node] = UndirectedGraphNode(node.label)
        while len(q) > 0:
            cur_node = q.popleft()
            for n in cur_node.neighbors:
                if n not in visited_copy:
                    q.append(n)
                    visited_copy[n] = UndirectedGraphNode(n.label)
                visited_copy[cur_node].neighbors.append(visited_copy[n])
        return visited_copy[node]
