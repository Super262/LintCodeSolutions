class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        in_degree, neighbors = self.get_in_degree_and_neighbors(prerequisites, numCourses)
        start_points = [x for x in in_degree if in_degree[x] == 0]
        import collections
        q = collections.deque(start_points)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for n in neighbors[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        if len(order) == numCourses:
            return True
        return False

    def get_in_degree_and_neighbors(self, graph: list, n: int) -> tuple:
        in_degree = {v: 0 for v in range(n)}
        neighbors = {v: [] for v in range(n)}
        for e in graph:
            in_degree[e[0]] += 1
            neighbors[e[1]].append(e[0])
        return in_degree, neighbors
