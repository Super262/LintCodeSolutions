class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, m: list) -> int:
        if not m or not m[0]:
            return 0
        visited = [False] * len(m)
        count = 0
        for i in range(len(m)):
            if m[i][i] == 1 and not visited[i]:
                self.bfs(m, visited, i)
                count += 1
        return count

    def bfs(self, m: list, visited: list, start: int) -> None:
        import collections
        q = collections.deque([start])
        while q:
            node = q.popleft()
            for i in range(len(m[node])):
                if m[i][i] == 0 or m[node][i] == 0 or visited[i]:
                    continue
                q.append(i)
                visited[i] = True
