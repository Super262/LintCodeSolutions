class Solution:

    def findCircleNum(self, M: list) -> int:
        if not M:
            return 0
        count = 0
        for i in range(len(M[0])):
            if M[i][i] == 1:
                self.bfs(M, i)
                count += 1
        return count

    def bfs(self, M: list, start: int) -> None:
        import collections
        q = collections.deque([start])
        while q:
            node = q.popleft()
            M[node][node] = 0
            for i in range(len(M[node])):
                if M[node][i] == 0 or M[i][i] == 0:
                    continue
                q.append(i)
